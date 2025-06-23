Step 1: Load Silver Layer Tables
silver_users = spark.table("silver_users")
silver_dest = spark.table("silver_destinations")

Step 2: Explode Arrays for Matching
from pyspark.sql.functions import explode, col

exploded_users = silver_users.select("user_id", "budget", explode("interests_array").alias("user_interest"))

exploded_dest = silver_dest.select("destination", "cost_level", explode("tags_array").alias("destination_tag"))

Step 3: Join Users with Destinations Based on Interests
user_dest_matches = exploded_users.join(exploded_dest, exploded_users.user_interest == exploded_dest.destination_tag, how="inner")

Step 4: Add a Match Score (count of matching interests)
from pyspark.sql.functions import count

match_scores = user_dest_matches.groupBy("user_id", "destination", "budget", "cost_level") \
    .agg(count("*").alias("match_score"))

Step 5: Filter on Budget Compatibility (Optional but smart)
final_recommendations = match_scores.filter(
    (col("budget") == col("cost_level")) | (col("cost_level") == "low")
)

Step 6: Save as Gold Table
final_recommendations.write.mode("overwrite").format("delta").saveAsTable("gold_user_recommendations")

Step 7: Show Results

spark.table("gold_user_recommendations").orderBy("user_id", "match_score", ascending = False).show(truncate=False)
