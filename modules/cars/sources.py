# import numpy as np
from PIL import Image

def get_sources_module(df, st, px):
    st.subheader(f"Najpopularniejsza marka pojazdów ze względu na pochodzenie (dane z lat 2010-2022)")
    image = Image.open("./assets/infographic_sources.png")
    st.image(image, caption="Infografika prezentująca najpopularniejsze marki pojazdów ze względu na pochodzenie")

    st.subheader("Marki pojazdów zakupionych od służb")
    df["Model"] = df["Model"].replace({"CEE'D": "CEED"})
    grouped = df[df["Source"] == "ZAKUPIONY OD SŁUŻB"].groupby(["Brand", "Model"]).size().reset_index(name="Count")
    grouped["FullName"] = grouped["Brand"].str.cat(grouped["Model"], sep=' ')
    grouped = grouped.sort_values("Count", ascending=False).head(10)
    fig = px.bar(grouped, x="FullName", y="Count")
    st.plotly_chart(fig)

    # Code below was used to prepare infographic
    # avaliable_sources = ['NOWY IMPORT INDYW', 'NOWY ZAKUPIONY W KRAJU', 'UŻYW. IMPORT INDYW', 'UŻYW. ZAKUPIONY W KRAJU', 'ZAKUPIONY OD SŁUŻB']
    #
    # years = list(range(df["Year"].min(), df["Year"].max()+1))
    #
    # col1, col2 = st.columns(2)
    # with col1:
    #     start = st.selectbox("Początek zakresu danych", years)
    # with col2:
    #     end = st.selectbox("Koniec zakresu danych", years, index=len(years)-1)
    #
    # selected_opts = st.multiselect('Pochodzenie pojazdu', avaliable_sources, avaliable_sources)
    #
    # most_popular_by_source = df[(df["Year"] >= start) & (df["Year"] <= end)].groupby(['Source', 'Brand']).size().reset_index(name='Count')
    # most_popular_by_source = most_popular_by_source.groupby('Source').apply(lambda x:x.nlargest(1, 'Count')).reset_index(drop=True)
    # most_popular_by_source = most_popular_by_source[most_popular_by_source["Source"].isin(selected_opts)]
    # most_popular_by_source = most_popular_by_source.sort_values("Count", ascending=False)
    #
    # y_pos = np.arange(len(selected_opts))
    # fig, ax = plt.subplots()
    # ax.bar(y_pos, most_popular_by_source["Count"])
    # ax.set_xticks(y_pos, most_popular_by_source["Source"])
    #
    # for i, value, brand in zip(range(len(most_popular_by_source)),most_popular_by_source["Count"], most_popular_by_source["Brand"]):
    #     ax.text(y_pos[i], value, f'{brand}\n({value})', ha='center', va='bottom', fontsize='4')
    #
    # fig.layout='tight'
    # ax.set_yscale("log")
    # ax.get_yaxis().set_visible(False)
    # ax.set_title("")
    # ax.set_xticklabels(most_popular_by_source["Source"], rotation=45, ha='right', fontsize='4') # pyright: ignore
    # fig.set_size_inches(6, 4)
    #
    # st.pyplot(fig)
