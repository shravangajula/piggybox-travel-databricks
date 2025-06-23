# PiggyBox Travel Recommender 🧳✨

An end-to-end data engineering project built on **Databricks**, using the **Bronze-Silver-Gold Lakehouse architecture** to power a **personalized travel recommendation engine**. This project was developed to showcase modern ETL workflows, data transformation in PySpark, and Delta Lake best practices on Databricks.

---

## 🧠 Problem Statement

Recommend travel destinations to users based on:
- Their interests
- Travel history
- Budget

Destinations are scored based on **tag overlap** and **budget compatibility**, and final recommendations are saved in the Gold layer.

---

## 🏗️ Architecture Overview

CSV Mock Data (Users, Destinations)
→
Bronze Layer (Raw Delta Tables)
→
Silver Layer (Cleaned & Enriched)
→
Gold Layer (Scored Recommendations)


---

## 📁 Folder Structure

piggybox-travel-databricks/
│
├── notebooks/
│ ├── 01_bronze_layer_ingestion.py # Load raw data and save as bronze Delta tables
│ ├── 02_silver_layer_transformations.py # Clean and explode interest/tag columns
│ └── 03_gold_user_recommendations.py # Match users to destinations and score
│
├── data/
│ ├── users_mock.csv # Mock user data (interests, travel history)
│ └── destinations.csv # Mock destination data (tags, cost, safety)
│
├── README.md
└── LICENSE



---

## 📊 Features

- 🔹 Built entirely on **Databricks Serverless**
- 🔹 Uses **Delta Lake** and **Unity Catalog**
- 🔹 Implements **match scoring** logic using PySpark
- 🔹 Budget-aware filtering for recommendations
- 🔹 Easily extendable to ML or dashboarding

---

## 🔧 Tech Stack

- 🧠 Databricks (Serverless Notebook)
- 🐍 PySpark (Data Transformations)
- 🗂️ Delta Lake (Bronze-Silver-Gold architecture)
- 📘 Unity Catalog (Table Management)

| user\_id | destination | budget | cost\_level | match\_score |
| -------- | ----------- | ------ | ----------- | ------------ |
| 5        | bali        | medium | low         | 2            |
| 5        | manali      | medium | medium      | 1            |
| 5        | goa         | medium | low         | 1            |
| 4        | paris       | high   | high        | 2            |
| 3        | bali        | low    | low         | 1            |
| 3        | goa         | low    | low         | 1            |
| 2        | manali      | medium | medium      | 1            |
| 1        | bali        | low    | low         | 1            |
| 1        | goa         | low    | low         | 1            |

---

## 🙋‍♂️ Author

**Shravan Kumar Gajula**  
Built as part of a Databricks portfolio project  
📫 [LinkedIn](https://www.linkedin.com/in/shravangajula)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Thank You

Thank you for taking the time to explore the PiggyBox Travel Recommender project!  
Whether you're a recruiter, fellow data engineer, or just someone curious about Databricks and travel tech — I appreciate your interest.  
Feel free to connect with me on LinkedIn or GitHub. I’m always open to feedback, collaboration, or just a friendly tech chat.

Happy Travels,  
**Shravan Gajula** 🌍✈️
