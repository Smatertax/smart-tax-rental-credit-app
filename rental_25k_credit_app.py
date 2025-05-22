
import streamlit as st

st.set_page_config(page_title="Smart Tax – $25K Rental Passive Loss Deduction Qualifier")

st.title("🏠 Do You Qualify for the $25,000 Rental Property Tax Break?")
st.markdown("The IRS allows certain rental property owners to deduct **up to $25,000** in passive losses from their ordinary income — if you qualify under income and activity rules. Let's find out if you're eligible.")

# Input fields
st.subheader("📋 Tell us about your rental situation")
income = st.number_input("Your Adjusted Gross Income (AGI)", min_value=0)
real_estate_hours = st.number_input("How many hours did you spend managing your rental this year?", min_value=0)
ownership_percent = st.slider("What % of the rental do you own?", 0, 100, 100)

filing_status = st.selectbox("Filing Status", ["Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household"])
rental_activity_type = st.selectbox("Your Involvement Level", [
    "I manage or materially participate in the rental",
    "I use a property manager and don't actively manage",
    "I’m unsure"
])

# Evaluation logic
def check_eligibility(agi, hours, ownership, status, activity_level):
    if agi > 150000:
        return "🚫 Not Eligible", "Your AGI exceeds the IRS phase-out limit of $150,000 for this deduction."
    elif agi > 100000:
        return "⚠️ Partially Eligible", "Your deduction may be reduced between AGI $100,000 and $150,000 due to phase-out rules."
    elif hours < 100 or activity_level != "I manage or materially participate in the rental":
        return "⚠️ Possibly Eligible", "You may qualify, but the IRS requires at least 100 hours and active participation to fully claim this credit."
    elif ownership < 10:
        return "⚠️ Unlikely Eligible", "You must own at least 10% of the property to qualify for the $25K passive loss deduction."
    else:
        return "✅ Likely Eligible", "You appear to meet the IRS requirements for claiming up to $25,000 in rental loss deductions."

# Output
if st.button("Check My Eligibility"):
    result, explanation = check_eligibility(income, real_estate_hours, ownership_percent, filing_status, rental_activity_type)
    st.subheader(result)
    st.write(explanation)

    if "Eligible" in result:
        st.markdown("🧾 **You may be entitled to deduct up to $25,000 of your rental losses this year.**")
        st.link_button("📅 Book a Smart Tax Rental Review", "https://calendly.com/clemscontractservice")
    else:
        st.markdown("📌 Let Smart Tax review your rental setup and show you other options.")
        st.link_button("👀 Schedule a Strategy Call", "https://calendly.com/clemscontractservice")

st.markdown("---")
st.caption("Smart Tax – Helping property owners maximize IRS credits legally and strategically.")
