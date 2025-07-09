#
 # @Date: 2025-06-26 16:59:55
 # @Author: thirky
 # @Description: 
 #
import tomlkit
import sys
sys.path.append(r'.\adapters')
from ExcelUtil import ExcelUtil
from TomlConfigGenerator import GatewayConfig, TomlConfigGenerator

def generate_toml_files(sheet_name: str, output_dir: str):
    """从Excel生成多个TOML文件"""
    configs = ExcelUtil.read_excel_config(sheet_name)
    
    for config in configs:
        # 创建网关配置
        gw_config = GatewayConfig(
            Gwid=config["网关ID"],
            Name=config["网关名称"],
            Prjcode=config["网关ID"],
            Prjname=config["网关名称"],
            Stationid=config["平台站点ID"]
        )
        
        # 初始化生成器
        generator = TomlConfigGenerator(gw_config)
        
        # 添加空调1
        if "空调1名称" in config and config["空调1名称"]:
            generator.add_air_conditioner(
                air_name=config["空调1名称"],
                model_id=str(config["空调1ModelID"])
            )
        
        # 添加空调2
        if "空调2名称" in config and config["空调2名称"]:
            generator.add_air_conditioner(
                air_name=config["空调2名称"],
                model_id=str(config["空调2ModelID"]),
            )
        
        # 添加储能电池
        generator.add_battery_devices(
            battery_type="storage",
            count=config["储能电池数量"],
            model_id=str(config["储能电池ModelID"])
        )
        
        # 添加备用电池
        generator.add_battery_devices(
            battery_type="backup",
            count=config["备用电池数量"],
            model_id=str(config["备用电池ModelID"])
        )
        
        # 生成TOML配置
        toml_config = generator.generate()
        
        # 写入文件
        output_path = f"{output_dir}/{config['网关名称']}.toml"
        with open(output_path, "w", encoding="utf-8") as f:
            tomlkit.dump(toml_config, f)
        
        print(f"已生成配置文件: {output_path}")