import streamlit as st
from sklearn.model_selection import KFold, StratifiedKFold

def render():
    st.markdown("## 🧠 Model Configuration")

    df = st.session_state.get("df")

    if df is None:
        st.warning("Please complete data preprocessing first.")
        return

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # ======================================================
    # 1️⃣ Task Type Selection
    # ======================================================
    st.subheader("🔍 Task Type")

    task_type = st.radio(
        "Select Learning Type",
        ["Supervised Learning", "Unsupervised Learning"]
    )

    # ======================================================
    # 2️⃣ Feature & Target Selection
    # ======================================================
    st.subheader("🧩 Feature Selection")

    features = st.multiselect("Select Feature Columns", df.columns)

    target = None
    if task_type == "Supervised Learning":
        target = st.selectbox("Select Target Column", df.columns)

    # ======================================================
    # 3️⃣ Train-Test Split
    # ======================================================
    st.subheader("📊 Train-Test Split")

    test_size = st.slider("Test Size", 0.1, 0.5, 0.2)
    random_state = st.number_input("Random State", value=42, step=1)

    # ======================================================
    # 4️⃣ Model Selection
    # ======================================================
    st.subheader("🤖 Model Selection")

    if task_type == "Supervised Learning":
        model_type = st.selectbox(
            "Select Problem Type",
            ["Classification", "Regression"]
        )

        if model_type == "Classification":
            models = [
                "Logistic Regression",
                "Random Forest Classifier",
                "Support Vector Machine",
                "K-Nearest Neighbors"
            ]
        else:
            models = [
                "Linear Regression",
                "Ridge Regression",
                "Lasso Regression",
                "Random Forest Regressor"
            ]

    else:
        models = [
            "KMeans",
            "DBSCAN",
            "Agglomerative Clustering",
            "PCA"
        ]

    selected_models = st.multiselect(
        "Select Model(s)",
        models
    )

    # ======================================================
    # 5️⃣ Hyperparameter Configuration (Dynamic)
    # ======================================================
    st.subheader("⚙️ Hyperparameter Configuration")

    model_params = {}

    for model in selected_models:
        with st.expander(f"{model} Parameters"):
            params = {}

            if model == "Logistic Regression":
                params["C"] = st.slider("C", 0.01, 10.0, 1.0)
                params["max_iter"] = st.slider("Max Iterations", 100, 1000, 300)

            elif model == "Random Forest Classifier":
                params["n_estimators"] = st.slider("Estimators", 50, 500, 100)
                params["max_depth"] = st.slider("Max Depth", 2, 30, 10)

            elif model == "Support Vector Machine":
                params["C"] = st.slider("C", 0.1, 10.0, 1.0)
                params["kernel"] = st.selectbox("Kernel", ["linear", "rbf", "poly"])

            elif model == "K-Nearest Neighbors":
                params["n_neighbors"] = st.slider("Neighbors", 1, 20, 5)

            elif model == "Linear Regression":
                params["fit_intercept"] = st.checkbox("Fit Intercept", True)

            elif model == "Ridge Regression":
                params["alpha"] = st.slider("Alpha", 0.1, 10.0, 1.0)

            elif model == "Lasso Regression":
                params["alpha"] = st.slider("Alpha", 0.01, 5.0, 1.0)

            elif model == "Random Forest Regressor":
                params["n_estimators"] = st.slider("Estimators", 50, 500, 100)
                params["max_depth"] = st.slider("Max Depth", 2, 30, 10)

            elif model == "KMeans":
                params["n_clusters"] = st.slider("Clusters", 2, 15, 3)

            elif model == "DBSCAN":
                params["eps"] = st.slider("Epsilon", 0.1, 5.0, 0.5)
                params["min_samples"] = st.slider("Min Samples", 2, 10, 5)

            elif model == "Agglomerative Clustering":
                params["n_clusters"] = st.slider("Clusters", 2, 15, 3)

            elif model == "PCA":
                params["n_components"] = st.slider(
                    "Components", 2, min(10, len(features)), 2
                )

            model_params[model] = params

    # ======================================================
    # 6️⃣ Cross Validation Configuration
    # ======================================================
    st.subheader("🔁 Cross Validation")

    enable_cv = st.checkbox("Enable Cross Validation")

    cv_config = None
    if enable_cv:
        cv_type = st.selectbox(
            "Cross Validation Strategy",
            ["K-Fold", "Stratified K-Fold"]
        )

        folds = st.slider("Number of Folds", 2, 10, 5)

        cv_config = {
            "type": cv_type,
            "folds": folds
        }

    # ======================================================
    # 7️⃣ Save Configuration
    # ======================================================
    st.session_state.model_config = {
        "task_type": task_type,
        "features": features,
        "target": target,
        "test_size": test_size,
        "random_state": random_state,
        "models": selected_models,
        "model_params": model_params,
        "cross_validation": cv_config
    }

    # ======================================================
    # 8️⃣ Navigation
    # ======================================================
    if st.button("➡️ Next: Training"):
        st.session_state.page = "Training"

    st.markdown('</div>', unsafe_allow_html=True)
