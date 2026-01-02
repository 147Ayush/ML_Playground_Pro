import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

def render():
    st.markdown("## 🧹 Data Preprocessing")

    if "df" not in st.session_state:
        st.session_state.df = None

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # =======================
    # Upload Dataset
    # =======================
    file = st.file_uploader("📂 Upload CSV Dataset", type="csv")

    if file:
        df = pd.read_csv(file)
        st.session_state.df = df.copy()

    if st.session_state.df is not None:
        df = st.session_state.df

        # =======================
        # Dataset Preview
        # =======================
        st.subheader("📊 Dataset Preview")
        st.dataframe(df, use_container_width=True)

        # =======================
        # Dataset Info
        # =======================
        with st.expander("ℹ️ Dataset Information"):
            st.write("Shape:", df.shape)
            st.write("Data Types:")
            st.dataframe(df.dtypes.astype(str))
            st.write("Summary Statistics:")
            st.dataframe(df.describe(include="all"))

        # =======================
        # Column Selection
        # =======================
        st.subheader("🗂 Column Management")

        drop_cols = st.multiselect(
            "Select columns to drop",
            df.columns
        )
        if drop_cols:
            df = df.drop(columns=drop_cols)

        # =======================
        # Missing Value Handling
        # =======================
        st.subheader("🚫 Missing Value Handling")

        col_mv = st.selectbox("Column", df.columns)
        strategy = st.selectbox(
            "Strategy",
            ["Mean", "Median", "Mode", "Drop Rows"]
        )

        if st.button("Apply Missing Value Strategy"):
            if strategy == "Mean":
                df[col_mv].fillna(df[col_mv].mean(), inplace=True)
            elif strategy == "Median":
                df[col_mv].fillna(df[col_mv].median(), inplace=True)
            elif strategy == "Mode":
                df[col_mv].fillna(df[col_mv].mode()[0], inplace=True)
            else:
                df.dropna(subset=[col_mv], inplace=True)

            st.success("Missing values handled")

        # =======================
        # Change Data Type
        # =======================
        st.subheader("🔁 Change Column Data Type")

        col_type = st.selectbox("Column to Convert", df.columns)
        new_type = st.selectbox("New Type", ["int", "float", "str"])

        if st.button("Convert Data Type"):
            try:
                df[col_type] = df[col_type].astype(new_type)
                st.success("Data type updated")
            except Exception as e:
                st.error(str(e))

        # =======================
        # Encoding
        # =======================
        st.subheader("🏷 Encoding")

        cat_cols = df.select_dtypes(include="object").columns.tolist()
        enc_cols = st.multiselect("Categorical Columns", cat_cols)

        enc_method = st.radio(
            "Encoding Method",
            ["One-Hot Encoding", "Label Encoding"]
        )

        if st.button("Apply Encoding"):
            if enc_method == "One-Hot Encoding":
                df = pd.get_dummies(df, columns=enc_cols)
            else:
                le = LabelEncoder()
                for col in enc_cols:
                    df[col] = le.fit_transform(df[col])

            st.success("Encoding applied")

        # =======================
        # Feature Scaling
        # =======================
        st.subheader("📐 Feature Scaling")

        num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        scale_cols = st.multiselect("Numerical Columns", num_cols)

        scaler_type = st.selectbox(
            "Scaling Method",
            ["StandardScaler", "MinMaxScaler"]
        )

        if st.button("Apply Scaling"):
            scaler = StandardScaler() if scaler_type == "StandardScaler" else MinMaxScaler()
            df[scale_cols] = scaler.fit_transform(df[scale_cols])
            st.success("Scaling applied")

        # =======================
        # Add New Column (Safe)
        # =======================
        st.subheader("➕ Create New Column")

        new_col = st.text_input("New Column Name")
        base_col = st.selectbox("Base Column", df.columns)
        operation = st.selectbox("Operation", ["Multiply by", "Add", "Subtract", "Divide by"])
        value = st.number_input("Value", value=1.0)

        if st.button("Create Column"):
            if operation == "Multiply by":
                df[new_col] = df[base_col] * value
            elif operation == "Add":
                df[new_col] = df[base_col] + value
            elif operation == "Subtract":
                df[new_col] = df[base_col] - value
            else:
                df[new_col] = df[base_col] / value

            st.success(f"Column `{new_col}` created")

        # =======================
        # Save State
        # =======================
        st.session_state.df = df

        # =======================
        # Download
        # =======================
        st.download_button(
            "⬇️ Download Processed Dataset",
            df.to_csv(index=False),
            file_name="processed_dataset.csv"
        )

        # =======================
        # Next Page
        # =======================
        if st.button("➡️ Next: Model Configuration"):
            st.session_state.page = "Model Config"

    st.markdown('</div>', unsafe_allow_html=True)
