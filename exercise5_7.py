# ID of product BRAND_NAME_MODEL_YEAR_MONTH_DAY_C_CATEGORY
products = (
    "PHILIPS_Boiler_HD4646_2020_09_21_C_1",
    "KENWOOD_KitchenMachine_KVL8300S_2015_09_22_C_3",
    "BOSCH_Blender_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Fridge_ERF4114AOW_2017_11_07_C_2"
)

# Loop to split all variables
# change category number to category name
for part in products:
   part = part.split("_")
   category = part[7]
   if category == "1":
       category = "Small electronics"
   elif category == "2":
       category = "Appliances"
   elif category == "3":
       category = "Blenders"
    # print the final result
   print(f"Brand: {part [0]}")
   print(f"Name and model: {part[1]} ({part[2]})")
   print(f"Category: {category}")
   print(f"Addition date:: {part[5]}.{part[4]}.{part[3]}")
   print()
