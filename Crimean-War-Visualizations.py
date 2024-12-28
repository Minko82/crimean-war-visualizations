# pip install -U altair vega_datasets


import altair as alt 
from vega_datasets import data

crimea = data.crimea()
crimea

crimea = crimea.melt(id_vars=['date'], value_vars=['wounds', 'other', 'disease'], var_name='cause', value_name='count')
crimea = crimea.sort_values('date')
crimea


wounds = crimea[crimea.cause == 'wounds']

wounds.head()


alt.Chart(wounds).mark_line().encode(
    x="date",
    y="count"
)


alt.Chart(crimea).mark_area().encode(
    x="date",
    y=alt.Y("count", title="Number of Deaths"), # the picture doesn't show the axis change, but I included it just in case
    color=("cause")
)


alt.Chart(wounds).mark_bar(
    size=14,
    color='#cfb77c'
  ).encode(
    x="date",
    y="count:Q",
  ).properties(
    width=400,
    height=400
)


alt.Chart(crimea).mark_bar().encode(
    x="date",
    y="count:Q",
    color="cause:N",
    tooltip=["cause", "count"]
)


alt.Chart(crimea).mark_bar().encode(
    y=("cause"),
    x=('sum(count):Q')
)

bars = alt.Chart(crimea).mark_bar().encode(
    y=alt.Y("cause:N", axis=alt.Axis(title="Cause", labels=False)),
    x=alt.X('sum(count):Q', title = "Total Deaths"),
)

labels = bars.mark_text(
    align='left',
    dx=2
).encode(
    text='cause'
)

bars + labels


alt.Chart(wounds).mark_bar().encode(
    x=alt.X('count:Q', bin=True, title="Number of Deaths Caused by Wounds"),
    y=alt.Y('count()', title="Count of Days")
)


alt.Chart(crimea).mark_bar().encode(
    x=alt.X('count:Q', bin=True, title="Number of Deaths"),
    y=alt.Y('count()', title="Count of Days"),
    column = "cause:N"
    # facet = alt.Facet('cause:N', columns=3)
) .properties(
    width=125,
    height=100
)



alt.Chart(crimea).mark_rect().encode(
    x=alt.X('yearmonth(date):T', title="Date (year-month-date)", axis=alt.Axis(format='%b %d, %Y')),
    y=alt.Y('cause:N', title="Cause"),
    color=alt.Color('sum(count):Q', title="Count"),
    tooltip=[
        alt.Tooltip('sum(count):Q', title=" ")
    ]
).properties (
    width = 600
)


alt.Chart(wounds).mark_bar().encode(
    x=alt.X('yearmonth(date)', title="Date"),
    y=alt.Y('count', title="Death Count"),
    color=alt.Color('count:Q',
                    scale=alt.Scale(scheme='reds'),
                    title="Death Count"),
    tooltip=[
        alt.Tooltip('yearmonthdate(date):T', title="Date"),
        alt.Tooltip('count:Q', title="Death Count")
    ]
) .properties (
    width=300
)