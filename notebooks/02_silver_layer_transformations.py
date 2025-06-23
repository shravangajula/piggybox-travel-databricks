# Clean, explode, and prepare arrays
Step 1:
bronze_users = spark.table("bronze_users");
bronze_dest = spark.table("bronze_destinations")

Step 2:
from pyspark.sql.functions import split

silver_users = (
     bronze_users
    .withColumn("interests_array", split("interests", ";")) \
    .withColumn("history_array", split("travel_history", ";"))
)

Step 3:
silver_dest = bronze_dest \
    .withColumn("tags_array", split("popular_tags", ";"))

Step 4:
# Write to silver_users and silver_destinations tables
silver_users.write.mode("overwrite").format("delta").saveAsTable("silver_users")
silver_dest.write.mode("overwrite").format("delta").saveAsTable("silver_destinations")

Step 5:
spark.table("silver_users").select("user_id", "interests_array", "history_array").show(truncate=False)
spark.table("silver_destinations").select("destination", "tags_array").show(truncate=False)
