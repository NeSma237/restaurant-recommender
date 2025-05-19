# Knowledge-Based Restaurant Recommender System

## Overview  
This project implements a knowledge-based restaurant recommendation system that suggests dining options based on explicit user preferences such as cuisine type, location, and budget. Unlike collaborative filtering methods, this system does **not** rely on past user behavior, effectively solving the cold start problem.

The system leverages detailed restaurant attributes from the Zomato Restaurants Dataset to deliver personalized recommendations with an interactive user interface built using Streamlit.

---

## Features  
- **Explicit User Preferences:** Filter restaurants by city, cuisine(s), and budget category (low, medium, high).  
- **Ranking Algorithm:** Combines user ratings and cost to score and rank recommendations.  
- **Interactive UI:** Sidebar for input preferences, dynamic recommendation display with explanations and Google Maps links.  
- **Feedback Collection:** Built-in user satisfaction surveys to collect qualitative feedback for continuous improvement.  
- **Evaluation:** Supports A/B testing and detailed evaluation reports.

---

## Dataset  
The system uses the publicly available Zomato Restaurants Dataset from Kaggle:  
[Zomato Restaurants Dataset](https://www.kaggle.com/datasets/shrutimehta/zomato-restaurants-data)

---

## Future Improvements
- Add proximity-based ranking using user location.

- Enhance filtering options with more cuisine and budget granularity.

- Integrate map visualizations directly into the UI.

- Implement machine learning for personalized recommendations based on implicit feedback.

---
## Installation  

1. Clone this repository:  
```bash
git clone https://github.com/NeSma237/restaurant-recommender.git
cd restaurant-recommender
---
