import streamlit as st
from BladesInTheDarkRoller.roller import Roller


st.markdown("# Blades in the Dark Roller")

r = Roller()

roll_types = ["Action", "Resistance", "Engagement", "Fortune"]
label = "Let’s roll…"

selected_roll = st.selectbox(
    label="What do you want to roll?",
    options=roll_types,
)

## action dice
if selected_roll == roll_types[0]:
    action_rating = st.selectbox(label="How many dice?", options=range(1, 6))

# Resistance dice
if selected_roll == roll_types[1]:
    resist_rating = st.selectbox(label="How many dice?", options=range(1, 6))

# Fortune dice
if selected_roll == roll_types[3]:
    advantageDice = st.selectbox(
        label="How many major advantages?", options=range(0, 4)
    )
    disadvantageDice = st.selectbox(
        label="How many major disadvantages?", options=range(0, 4)
    )
    fortune_dice = 1 + advantageDice - disadvantageDice
    st.markdown(
        f"The number of dice is {fortune_dice}. Hit the **{label}** button when you are ready."
    )

# Engagement dice
if selected_roll == roll_types[2]:
    engagementDice = 1
    bold = st.checkbox("This operation particularly bold or daring.")
    if bold:
        engagementDice += 1
        st.markdown("+1 advantage dice.")
    complex = st.checkbox(
        "This operation overly complex or contingent on many factors."
    )
    if complex:
        engagementDice -= 1
        st.markdown("-1 advantage dice.")
    vulnerable = st.checkbox(
        "The plan's detail expose a vulnerability of the target or hit them where they're weakest."
    )
    if vulnerable:
        engagementDice += 1
        st.markdown("+1 advantage dice.")
    defended = st.checkbox(
        "The target strongest against this approach, or they have particular defenses or special defenses or special preparations. "
    )
    if defended:
        engagementDice -= 1
        st.markdown("-1 advantage dice.")
    aid = st.checkbox(
        "Some friends or contacts provide aid or insight for this operation."
    )
    if aid:
        engagementDice += 1
        st.markdown("+1 advantage dice.")
    interference = st.checkbox("Enemies or rivals are interfering in the operation.")
    if interference:
        engagementDice -= 1
        st.markdown("-1 advantage dice.")
    otherFactors = st.selectbox(
        "Is there any other factor to consider? Input 0, or a positive/negative number for advantage / disadvantage respectively. ",
        options=range(-2, 3),
        index=2,
    )
    engagementDice += otherFactors

    st.markdown(
        f"The dice pool is **{engagementDice}**. Hit the **{label}** button when you are ready."
    )
# action roll
if selected_roll == roll_types[0] and st.button(label=label):
    result = r.actionRoll(action_rating)
    st.markdown(result)

# Resistance roll
if selected_roll == roll_types[1] and st.button(label=label):
    result = r.resistanceRoll(resist_rating)
    st.markdown(result)

# Engagement roll
if selected_roll == roll_types[2] and st.button(label=label):
    result = r.engagementRoll(engagementDice)
    st.markdown(result)

# Fortune roll
if selected_roll == roll_types[3] and st.button(label=label):
    result = r.fortuneRoll(fortune_dice)
    st.markdown(result)
