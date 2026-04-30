#!/usr/bin/env python3
"""
Data Science Final Exam Practice Quiz - FREE RESPONSE FORMAT
Practice explaining concepts like you'll do on the actual exam
Run: python practice_quiz.py
"""

import os
import sys

# Free response questions with model answers
QUESTIONS = [
    {
        "num": 1,
        "section": "Data Science Fundamentals",
        "question": "Explain the Pi-Model. What does it represent and why is it important for data scientists?",
        "model_answer": "The Pi-Model represents the skill structure data scientists should develop. The vertical bar shows depth in 2-3 specialized areas (like machine learning or statistics), while the horizontal bar shows breadth across many other areas (business, communication, domain knowledge, etc.). It's important because data scientists need deep expertise to solve complex problems while being knowledgeable enough across domains to communicate effectively and understand different perspectives."
    },
    {
        "num": 2,
        "section": "Data Science Fundamentals",
        "question": "What does it mean that 'the data tells the story, not the scientist'? Give an example of what happens when this principle is violated.",
        "model_answer": "This means data scientists should follow what the data reveals through objective analysis, not force a predetermined narrative onto it. When violated, a scientist might selectively highlight data that supports their hypothesis while ignoring contradictory evidence. For example, a scientist studying drug effectiveness might only report positive results while burying adverse effects, biasing the conclusion toward what they wanted to find rather than the truth the data shows."
    },
    {
        "num": 3,
        "section": "Data Science Fundamentals",
        "question": "List and briefly describe the 6 phases of the CRISP-DM process.",
        "model_answer": "1) Business Understanding - Define the problem and objectives\n2) Data Understanding - Explore, assess quality, identify patterns\n3) Data Preparation - Clean, transform, engineer features\n4) Modeling - Select and train machine learning models\n5) Evaluation - Assess performance, validate results\n6) Deployment - Put the model into production and monitor it"
    },
    {
        "num": 4,
        "section": "ETL & Data Wrangling",
        "question": "When would you drop a column with missing values vs. filling missing values vs. keeping missing as an indicator? Give specific examples for each.",
        "model_answer": "DROP: When >50% of data is missing (too much information lost). Example: A sensor column with 80% missing readings.\nFILL: When missing is random/ignorable. Example: A few missing salary values filled with mean salary.\nKEEP AS INDICATOR: When the missingness itself is meaningful. Example: If a sensor stops reporting at night, the 'missing' IS the information (nighttime). You'd create a binary 'is_nighttime' feature."
    },
    {
        "num": 5,
        "section": "ETL & Data Wrangling",
        "question": "Explain the difference between one-hot encoding, ordinal encoding, and label encoding. When would you use each?",
        "model_answer": "ONE-HOT: Creates binary (0/1) columns for each category. Example: Color→{Red:[1,0,0], Blue:[0,1,0]}. Use for unordered categories (colors, names).\nORDINAL: Assigns ordered numbers. Example: Size→{Small:1, Medium:2, Large:3}. Use when categories have inherent order.\nLABEL: Simple numerical mapping without assumption of order. Example: City→{NYC:0, LA:1}. Use sparingly; can introduce false ordering."
    },
    {
        "num": 6,
        "section": "ETL & Data Wrangling",
        "question": "What is a JOIN and what's the difference between LEFT JOIN, INNER JOIN, and OUTER JOIN?",
        "model_answer": "A JOIN combines two tables horizontally using a common key. LEFT JOIN: Keeps all rows from left table + matching rows from right (unmatched right rows become NULL). INNER JOIN: Only keeps rows that exist in BOTH tables. OUTER JOIN: Keeps all rows from both tables (unmatched become NULL). LEFT is most common because you keep your primary data even if there's no match."
    },
    {
        "num": 7,
        "section": "EDA & Statistics",
        "question": "What is the purpose of EDA and how does it fit into the CRISP-DM process? List 3 things you discover during EDA.",
        "model_answer": "EDA (Exploratory Data Analysis) aims to understand data structure, patterns, and quality BEFORE modeling. It bridges 'Data Understanding' and 'Data Preparation' phases. Three discoveries: 1) Distribution of variables and outliers (informs if data needs transformation), 2) Relationships between features and target (guides feature selection), 3) Data quality issues like missing values (informs cleaning strategy)."
    },
    {
        "num": 8,
        "section": "EDA & Statistics",
        "question": "Explain correlation and covariance. What is the key difference between them? Can you have high correlation but no causation?",
        "model_answer": "COVARIANCE: Measures how two variables move together (unbounded, hard to interpret). CORRELATION: Standardized covariance, ranges -1 to 1 (easy to compare). Key difference: Correlation is scaled/normalized, covariance isn't. YES - you can absolutely have high correlation without causation (spurious correlation). Example: Ice cream sales correlate with drowning deaths (both driven by summer weather), but ice cream doesn't cause drowning."
    },
    {
        "num": 9,
        "section": "Statistical Learning",
        "question": "In the equation y = f(x) + ε, what does each component represent? What happens if you try to model ε?",
        "model_answer": "y = target variable\nf(x) = true underlying function\nε = irreducible error (random noise, unmeasured factors)\nIf you try to model ε, you OVERFIT. You're trying to explain random noise rather than true patterns. The model memorizes noise in training data and fails on new data."
    },
    {
        "num": 10,
        "section": "Regression",
        "question": "What is the purpose of regression? Give an example. Then explain what MAE and RMSE measure and when you might prefer one over the other.",
        "model_answer": "PURPOSE: Predict a continuous numerical value from input features. EXAMPLE: Predicting house prices from square footage, bedrooms, location. MAE (Mean Absolute Error): Average absolute error in original units - easy to interpret, robust to outliers. RMSE (Root Mean Squared Error): Square root of average squared errors - penalizes large errors heavily. Use MAE when outliers are valid and shouldn't be penalized extra; use RMSE when large errors are especially bad."
    },
    {
        "num": 11,
        "section": "Regression",
        "question": "What are variance, covariance, and correlation in the context of linear regression? What does each tell you?",
        "model_answer": "VARIANCE: Spread of data around the mean - high variance means values are scattered. COVARIANCE: How much two variables move together (positive/negative direction). CORRELATION: Standardized version of covariance (-1 to 1). In linear regression, they show the strength and direction of the linear relationship between a feature and target. Correlation helps you quickly identify which features might be useful for predicting the target."
    },
    {
        "num": 12,
        "section": "Classification",
        "question": "What is classification? How is it different from regression? Give two examples.",
        "model_answer": "CLASSIFICATION: Predicts which category/class something belongs to (discrete output). Different from regression because regression predicts numbers (continuous). EXAMPLES: 1) Email spam detection (spam/not spam), 2) Tumor classification (malignant/benign). Classifiers are trained on labeled data where the category is known."
    },
    {
        "num": 13,
        "section": "Classification - kNN",
        "question": "Explain how k-Nearest Neighbors (kNN) makes predictions. What does the parameter k represent and how do you choose it?",
        "model_answer": "kNN finds the k training points closest to the new point, then predicts the most common class among those k neighbors (majority vote). k is the number of neighbors to consider. If k=1, very sensitive to individual points (overfitting). If k=100, too smooth/general. Common heuristic: k ≈ √n rounded to nearest prime number. Must be odd to avoid ties in binary classification."
    },
    {
        "num": 14,
        "section": "Classification - kNN",
        "question": "What are norms and why do they matter for kNN? Explain Euclidean and Manhattan distance.",
        "model_answer": "NORMS: Formulas for calculating distance between points. They matter for kNN because distance determines which neighbors are 'closest'. EUCLIDEAN (L2): √(Σ(differences²)) - straight-line distance (most common). MANHATTAN (L1): Σ|differences| - block/taxicab distance. Choice affects which points are considered neighbors. Euclidean is more common but Manhattan can be better for sparse data."
    },
    {
        "num": 15,
        "section": "Classification Metrics",
        "question": "Define Precision, Recall, Accuracy, and F1-Score. When would you prioritize Precision vs. Recall?",
        "model_answer": "ACCURACY: (TP+TN)/Total - simple but misleading with imbalanced data. PRECISION: TP/(TP+FP) - of predicted positives, how many were correct? (false positives are costly). RECALL: TP/(TP+FN) - of actual positives, how many did we catch? (false negatives are costly). F1-SCORE: Harmonic mean balancing both. USE PRECISION WHEN: False positives are expensive (spam filtering - don't annoy users). USE RECALL WHEN: False negatives are expensive (cancer detection - don't miss cases)."
    },
    {
        "num": 16,
        "section": "Clustering",
        "question": "What is clustering and how is it different from classification? Is it supervised or unsupervised? Why?",
        "model_answer": "CLUSTERING: Find natural groupings in data. DIFFERENT FROM CLASSIFICATION: Clustering has no predefined categories (unsupervised); classification predicts known categories (supervised). UNSUPERVISED because: We don't have labeled examples. The model discovers categories from the data structure itself. EXAMPLE: Customer segmentation - we don't know what segments exist, k-Means finds them."
    },
    {
        "num": 17,
        "section": "Clustering - k-Means",
        "question": "Explain how k-Means clustering algorithm works step-by-step.",
        "model_answer": "1) Choose k (number of clusters) - usually based on domain knowledge or Elbow Method\n2) Randomly initialize k cluster centers\n3) Assign each data point to its nearest cluster center\n4) Recalculate cluster centers as the mean of all assigned points\n5) Repeat steps 3-4 until convergence (centers stop moving)\nResult: Data divided into k tight, compact clusters."
    },
    {
        "num": 18,
        "section": "Clustering Metrics",
        "question": "What is WCSS (Within-Cluster Sum of Squares) and how does the Elbow Method help choose k?",
        "model_answer": "WCSS: Sum of squared distances from each point to its cluster center. Lower WCSS = tighter, more compact clusters = better clustering. WCSS always decreases as k increases (more clusters = tighter fit). ELBOW METHOD: Plot WCSS vs k. Look for the 'elbow' - where WCSS stops decreasing sharply. The elbow point indicates optimal k. Before the elbow, adding clusters helps a lot. After, adding clusters helps little."
    },
    {
        "num": 19,
        "section": "Feature Scaling",
        "question": "Why is feature scaling important? Explain the problem it solves with a specific example.",
        "model_answer": "PROBLEM: Distance-based algorithms (kNN) are affected by variable scale. If one variable has huge values and another small values, large-scale variables dominate. EXAMPLE: Years of experience (1-40) vs. Salary ($50,000-$150,000). Distance = √((exp_diff)² + (salary_diff)²). Salary differences are huge, completely drowning out experience differences. The algorithm treats experience as irrelevant even if it's actually important."
    },
    {
        "num": 20,
        "section": "Feature Scaling",
        "question": "Explain Normalization (Min-Max Scaling) and Standardization (Z-score). When would you use each?",
        "model_answer": "NORMALIZATION: (x - min)/(max - min) → scales to [0, 1]. Bounds output, uniform distribution. Use when: You need values in a specific range [0, 1], or data doesn't follow normal distribution. STANDARDIZATION: (x - mean)/std_dev → mean=0, std=1, normal distribution. Use when: Data should follow normal distribution, or algorithm assumes normal distribution (like some neural networks). Both preserve relative relationships between points."
    },
    {
        "num": 21,
        "section": "Cross-Validation",
        "question": "Why do we split data into training and test sets? What problem does this solve? What happens if you test on the same data you trained on?",
        "model_answer": "We split to detect OVERFITTING. Training set teaches the model. Test set evaluates on NEW unseen data. PROBLEM SOLVED: A model can memorize training data without learning real patterns. If you test on training data, the model gets high scores even though it won't generalize to new data. Train/test split catches this - model that memorized training will fail badly on test set."
    },
    {
        "num": 22,
        "section": "Real-World Application",
        "question": "You're building a model to predict whether a customer will churn (leave). Is this regression or classification? What metric would you prioritize and why?",
        "model_answer": "CLASSIFICATION - output is categorical (churn/no churn). METRIC: Prioritize RECALL. Why: False negatives (missing a churn risk) are very costly - you lose that customer. False positives (predicting churn when they won't) are cheaper - you send them an offer. High recall ensures you catch most customers at risk even if you send unnecessary offers to some."
    },
    {
        "num": 23,
        "section": "Real-World Application",
        "question": "A company has customer data but doesn't know how to segment them. Should they use classification, regression, or clustering? Explain your choice.",
        "model_answer": "CLUSTERING. Why: They have no predefined customer categories (no labels). Clustering discovers natural groups in the data unsupervised. Classification requires labeled training data (knowing which customers belong to which segment). Once clustering finds k customer segments, they can understand what each segment represents and use that for future classification."
    },
    {
        "num": 24,
        "section": "Data Wrangling",
        "question": "Explain the difference between long-format and wide-format data. When would you reshape from one to the other?",
        "model_answer": "LONG-FORMAT: One observation per row (typically preferred for analysis). More rows, fewer columns. WIDE-FORMAT: Multiple observations per row. Fewer rows, many columns. RESHAPE TO LONG: When data is too wide - easier to analyze, visualize, model. RESHAPE TO WIDE: When you need to compare variables side-by-side or for specific analyses. Example: Customer data - long has one row per purchase; wide has one row per customer with many purchase columns."
    },
    {
        "num": 25,
        "section": "EDA & Outliers",
        "question": "Should outliers always be removed during data cleaning? Explain with examples.",
        "model_answer": "NO. Outliers should be INVESTIGATED, not automatically removed. VALID OUTLIERS: Rare but real events (e.g., CEO salary in employee data is legitimately high). Removing deletes real information. INVALID OUTLIERS: Data entry errors (typo: age=2000). These should be removed/corrected. INFLUENTIAL OUTLIERS: Affect the model significantly. May be valid but worth noting. KEY: Understand WHY it's an outlier before deciding. Remove only if it's definitely an error."
    }
]


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')


def display_question(question_data, question_num, total_questions):
    """Display a single question"""
    clear_screen()
    print(f"\n{'='*75}")
    print(f"Question {question_num}/{total_questions} - {question_data['section']}")
    print(f"{'='*75}\n")
    print(f"Q{question_data['num']}: {question_data['question']}\n")
    print("Type your answer (write as much as you think is needed):")
    print("-" * 75)


def get_answer():
    """Get user's free response answer"""
    lines = []
    print("(Press Enter twice to finish your answer)")
    empty_lines = 0

    while True:
        try:
            line = input()
            if line == "":
                empty_lines += 1
                if empty_lines >= 2:
                    break
                lines.append("")
            else:
                empty_lines = 0
                lines.append(line)
        except EOFError:
            break

    return "\n".join(lines).strip()


def show_feedback(question_data, user_answer):
    """Show model answer and feedback"""
    clear_screen()
    print(f"\n{'='*75}")
    print("MODEL ANSWER")
    print(f"{'='*75}\n")
    print(question_data['model_answer'])
    print(f"\n{'='*75}")
    print("YOUR ANSWER")
    print(f"{'='*75}\n")
    print(user_answer if user_answer else "(blank)")
    print(f"\n{'='*75}")
    print("\nKey points to consider:")
    print("- Did you cover the main concepts?")
    print("- Did you provide specific examples or explanations?")
    print("- Compare your answer to the model answer above")
    print(f"{'='*75}\n")

    input("Press Enter to continue to the next question...")


def run_quiz():
    """Run the complete practice quiz"""
    clear_screen()
    print("\n" + "="*75)
    print("DATA SCIENCE FINAL EXAM PRACTICE QUIZ - FREE RESPONSE FORMAT")
    print("="*75)
    print("\nThis quiz matches the exam format - free response questions")
    print("about concepts. Answer as thoroughly as you would on the real exam.")
    print(f"\nTotal questions: {len(QUESTIONS)}\n")
    print("⚠️  REMEMBER: This is practice! Mistakes here help you prepare.")
    print("    Compare your answers to the model answers provided.\n")
    input("Press Enter to start...")

    completed = 0

    for idx, question in enumerate(QUESTIONS, 1):
        display_question(question, idx, len(QUESTIONS))
        user_answer = get_answer()

        show_feedback(question, user_answer)
        completed = idx

    # Summary
    clear_screen()
    print("\n" + "="*75)
    print("QUIZ COMPLETE")
    print("="*75 + "\n")

    print(f"You completed {completed}/{len(QUESTIONS)} questions!\n")

    print("NEXT STEPS:")
    print("1. Review any questions where your answer was incomplete")
    print("2. Study the concepts that were weak in your responses")
    print("3. Use the FINAL_STUDY_GUIDE.md to refresh on difficult topics")
    print("4. Retake this quiz or do a new practice run\n")

    print("="*75)
    print("Good luck on your exam tomorrow at 7 AM! 🚀")
    print("="*75 + "\n")

    # Ask if they want to retake
    while True:
        retake = input("Would you like to retake the quiz? (yes/no): ").strip().lower()
        if retake in ['yes', 'y']:
            run_quiz()
            break
        elif retake in ['no', 'n']:
            print("\nYou're well prepared! Get some rest and ace that exam! 📚\n")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nQuiz interrupted. Review the study guide and good luck! 📚\n")
        sys.exit(0)
