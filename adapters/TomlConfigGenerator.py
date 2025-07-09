#
 # @Date: 2025-06-25 17:24:53
 # @Author: thirky
 # @Description: 
 #

from openpyxl import load_workbook
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class ComParam:
    BaudRate: int = 9600
    DataBits: int = 8
    StopBits: int = 1
    Parity: str = "N"
    Timeout: int = 60

@dataclass
class CollectConfig:
    ID: str
    Mode: int = 1
    Type: str = "COM"
    Resend: int = 2
    SwInterval: int = 20
    Param: ComParam = field(default_factory=ComParam)

@dataclass
class FixedDevice:
    ID: int
    Name: str
    ModelID: str
    Port: str
    ComID: int
    Addr: str
    Interval: int = 1000
    Timeout: int = 1000
    Offline: int = 30

@dataclass
class BatteryDevice:
    ID: int
    Name: str
    ModelID: str
    Port: str
    ComID: int
    Addr: str
    Interval: int = 1000
    Timeout: int = 1000
    Offline: int = 30

@dataclass
class AirConditionerDevice:
    ID: int
    Name: str
    ModelID: str
    Port: str
    ComID: int
    Addr: str
    Interval: int = 1000
    Timeout: int = 1000
    Offline: int = 10

@dataclass
class ForwardParams:
    IP: str = "www.jrie.com.cn"
    Port: int = 1883
    User: str = "admin"
    Password: str = "admin123"
    Appid: str = "jinrong"
    Prjcode: str = ""
    Prjname: str = ""
    Stationid: str = ""
    Interval: int = 60
    History: int = 100
    IpAddr: str = "120.79.38.76"

@dataclass
class ForwardConfig:
    ID: str = "JR"
    Name: str = "JR"
    Protocol: str = "MqttDF"
    Enable: int = 1
    Certificate: str = "mcloud.pem"
    Params: ForwardParams = field(default_factory=ForwardParams)

@dataclass
class GatewayConfig:
    Gwid: str
    Name: str
    Prjcode: str
    Prjname: str
    Stationid: str
    Model: str = "GW200F"
    HwVer: str = "1.3"
    SwVer: str = "V1.0.34 20250307"
    
    def to_dict(self):
        return {
            "Gateway": {
                "Gwid": self.Gwid,
                "Name": self.Name,
                "Model": self.Model,
                "SN": "",
                "Date": "",
                "HwVer": self.HwVer,
                "SwVer": self.SwVer
            }
        }
    
class TomlConfigGenerator:
    """toml配置生成器类"""
    # 固定不变的串口配置
    COM_CONFIGS = [
        CollectConfig(ID="COM1", Param=ComParam(BaudRate=2400, Parity="E")),
        CollectConfig(ID="COM2"),
        CollectConfig(ID="COM3"),
        CollectConfig(ID="COM4", Resend=0, SwInterval=0),
        CollectConfig(ID="COM5", Param=ComParam(Timeout=40)),
        CollectConfig(ID="COM6", Param=ComParam(Timeout=40)),
        CollectConfig(ID="COM7", Param=ComParam(Timeout=40)),
        CollectConfig(ID="COM8", Param=ComParam(Timeout=40)),
        CollectConfig(ID="COM9", Param=ComParam(Timeout=40)),
        CollectConfig(ID="VT1", Type="VT", Param=ComParam(Timeout=1000))
    ]
    
    # 固定不变的设备
    FIXED_DEVICES = [
        FixedDevice(ID=1, Name="总进线计量", ModelID="11006", Port="COM1", ComID=1, Addr="1"),
        FixedDevice(ID=2, Name="电源1计量", ModelID="11006", Port="COM1", ComID=1, Addr="2"),
        FixedDevice(ID=3, Name="电源2计量", ModelID="11006", Port="COM1", ComID=1, Addr="3"),
        FixedDevice(ID=9, Name="空调节能控制器", ModelID="11000", Port="VT1", ComID=80, Addr="1"),
        FixedDevice(ID=10, Name="电池节能控制器", ModelID="11001", Port="VT1", ComID=80, Addr="1")
    ]
    
    def __init__(self, gw_config: GatewayConfig):
        self.gw_config = gw_config
        self.devices = []
        self.air_conditioners = []
        self.aircon_id = 5
        self.forward_config = ForwardConfig(
            Params=ForwardParams(
                Prjcode=gw_config.Prjcode,
                Prjname=gw_config.Prjname,
                Stationid=gw_config.Stationid
            )
        )
    def add_air_conditioner(self, air_name: str, model_id: str, port: str = "COM2", com_id: int = 2, addr: str = None):
        """添加空调设备
        Args:
            air_name: 名称(如"格力"、"美的")
            model_id: 设备型号ID
            port: 串口(默认为COM4)
            com_id: 同上
            addr: 设备地址(默认自动递增，格力空调默认为4)
        """
        if addr is None and "格力" in air_name:
            addr = "4"

        if addr is None:
            addr = str(1 + len(self.air_conditioners))  # 自动分配地址
        
        device = AirConditionerDevice(
            ID=self.aircon_id,
            Name=f"{air_name}",
            ModelID=model_id,
            Port=port,
            ComID=com_id,
            Addr=addr
        )
        
        self.air_conditioners.append(device)
        self.devices.append(device)
        self.aircon_id += 1  # 递增ID
        
        return device  # 返回创建的设备对象

    def add_battery_devices(self, battery_type: str, count: int, model_id: str):
        """添加电池设备(储能或备用)"""
        base_id = 20 if battery_type == "storage" else 40
        port = "COM5" if battery_type == "storage" else "COM6"
        com_id = 5 if battery_type == "storage" else 6
        
        for i in range(1, count + 1):
            device = BatteryDevice(
                ID=base_id + i - 1,
                Name=f"{'储能' if battery_type == 'storage' else '备用'}电池{i}",
                ModelID=model_id,
                Port=port,
                ComID=com_id,
                Addr=str(i + 1)  # Addr从2开始
            )
            self.devices.append(device)

    def generate(self) -> dict:
        """生成完整的TOML配置字典"""
        config = self.gw_config.to_dict()
        
        # 添加固定设备
        for device in self.FIXED_DEVICES:
            self.devices.append(device)
        
        # 设备列表
        config["Device"] = [self._device_to_dict(d) for d in self.devices]
        
        # 串口配置
        config["Collect"] = [self._collect_to_dict(c) for c in self.COM_CONFIGS]
        
        # Forward配置
        config["Forward"] = [{
            "ID": self.forward_config.ID,
            "Name": self.forward_config.Name,
            "Protocol": self.forward_config.Protocol,
            "Enable": self.forward_config.Enable,
            "Certificate": self.forward_config.Certificate,
            "Params": {
                "IP": self.forward_config.Params.IP,
                "Port": self.forward_config.Params.Port,
                "User": self.forward_config.Params.User,
                "Password": self.forward_config.Params.Password,
                "Appid": self.forward_config.Params.Appid,
                "Prjcode": self.forward_config.Params.Prjcode,
                "Prjname": self.forward_config.Params.Prjname,
                "Stationid": self.forward_config.Params.Stationid,
                "Interval": self.forward_config.Params.Interval,
                "History": self.forward_config.Params.History,
                "IpAddr": self.forward_config.Params.IpAddr
            }
        }]
        
        # EMS配置(固定)
        config["EMS"] = {
            "Bat": {
                "ems/bat1": {
                    "CtrlMode": 0,
                    "ModuleCtrl": 0,
                    "VFCc": 53.6,
                    "VBCc": 56.5,
                    "VFCd": 50.0,
                    "VBCd": 50.1,
                    "Vhigh": 57.5,
                    "Vlow": 46.0,
                    "BatCap": 400.0,
                    "CC": 10.0,
                    "RSOC": 10.0,
                    "MSOC": 80.0,
                    "TChgAuto": 0,
                    "TChgRetry": 20
                }
            },
            "Air": {
                "CtrlMode": 0,
                "TsAir": 30,
                "TpAir": 30,
                "Tf1Air": 25,
                "Tf2Air": 25,
                "Tf3Air": 30,
                "TvAir": 20
            }
        }
        
        return config

    def _device_to_dict(self, device) -> dict:
        return {
            "ID": device.ID,
            "Name": device.Name,
            "ModelID": device.ModelID,
            "Port": device.Port,
            "ComID": device.ComID,
            "Addr": device.Addr,
            "Interval": device.Interval,
            "Timeout": device.Timeout,
            "Offline": device.Offline
        }

    def _collect_to_dict(self, collect) -> dict:
        return {
            "ID": collect.ID,
            "Mode": collect.Mode,
            "Type": collect.Type,
            "Resend": collect.Resend,
            "SwInterval": collect.SwInterval,
            "Param": {
                "BaudRate": collect.Param.BaudRate,
                "DataBits": collect.Param.DataBits,
                "StopBits": collect.Param.StopBits,
                "Parity": collect.Param.Parity,
                "Timeout": collect.Param.Timeout
            }
        }