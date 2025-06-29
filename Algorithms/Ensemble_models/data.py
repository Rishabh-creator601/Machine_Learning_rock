from seedtools import load_seed,dropper,mapper_auto
import pandas as pd



cars  = load_seed("cars.csv","v2",quiet=True) 


# cols_ = ['feature_0','feature_1','feature_2','feature_3','feature_4','feature_5','feature_6','feature_7','feature_8','feature_9','manufacturer_name','model_name','location_region','year_produced','color','body_type','up_counter',"number_of_photos","duration_listed"]
# keys =  ["transmission","drivetrain","engine_fuel","engine_type","state","is_exchangeable","has_warranty","engine_has_gas"]

# keys_map =  {k:"auto"  for k in keys}



print(cars.data.columns.to_list())
