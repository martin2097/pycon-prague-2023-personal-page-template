import dash_mantine_components as dmc
from dash import dcc, html
from dash_iconify import DashIconify
import pandas as pd


def responzivny_stlpec_uprostred(obsah):
    """Vytvorí responzívny stĺpec uprostred obrazovky.

    Parametre:
    obsah - akákoľvek Dash komponenta alebo list Dash komponent
    """
    return (
        dmc.Grid(
            dmc.Col(
                obsah,
                span=10,
                sm=8,
                xl=6,
                offset=1,
                offsetSm=2,
                offsetXl=3,
                p=0,
            ),
            m=0,
        ),
    )


def nerespoznivny_navigacny_panel(odkazy, logo):
    """Vytvorí navigačný panel, ktorý však nie je prispôsobený mobilným zariadeniam.

    Parametre:
    odkazy - dictionary of dictionaries, prvým kľúčom je url odkaz, vnorený slovník očakáva kľúč label, ktorý sa zobrazí
     v Navigačnom panely
    logo - názov ikony z knižníc Iconify, ktorá bude použitá ako logo stránky
    """
    return dmc.Header(
        children=[
            dmc.Group(
                [
                    dcc.Link(
                        dmc.ActionIcon(
                            DashIconify(
                                icon=logo,
                                height=35,
                                width=35,
                            ),
                            variant="transparent",
                        ),
                        href="/",
                    ),
                    dmc.Group(
                        [
                            dmc.NavLink(
                                label=odkazy[link]["label"],
                                href=link,
                                style={
                                    "padding": "7px",
                                    "width": "auto",
                                },
                                styles={
                                    "label": {
                                        "color": "#868E96",
                                        "font-weight": "500",
                                        "font-size": "16px",
                                    },
                                },
                            )
                            for link in odkazy
                        ],
                        position="right",
                    ),
                ],
                position="apart",
                style={"margin-right": "2vh", "margin-left": "2vh"},
            )
        ],
        height=40,
        fixed=True,
        style={"margin-bottom": "3px"},
        withBorder=False,
    )


def navigacny_panel(odkazy, logo):
    """Vytvorí responzívny navigačný panel.

    Parametre:
    odkazy - dictionary of dictionaries, prvým kľúčom je url odkaz, vnorený slovník očakáva kľúč label, ktorý sa zobrazí
     v Navigačnom panely
    logo - názov ikony z knižníc Iconify, ktorá bude použitá ako logo stránky
    """
    return dmc.Header(
        children=[
            dmc.Stack(
                dmc.Group(
                    [
                        dcc.Link(
                            dmc.ActionIcon(
                                DashIconify(
                                    icon=logo,
                                    height=35,
                                    width=35,
                                ),
                                variant="transparent",
                                id={"type": "odkaz-menu", "index": "logo"},
                            ),
                            href="/",
                        ),
                        dmc.Group(
                            [
                                dmc.MediaQuery(
                                    dmc.NavLink(
                                        label=odkazy[link]["label"],
                                        href=link,
                                        style={
                                            "padding": "7px",
                                            "width": "auto",
                                        },
                                        styles={
                                            "label": {
                                                "color": "#868E96",
                                                "font-weight": "500",
                                                "font-size": "16px",
                                            },
                                        },
                                    ),
                                    smallerThan="sm",
                                    styles={"display": "none"},
                                )
                                for link in odkazy
                            ]
                            + [
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="radix-icons:blending-mode",
                                        width=25,
                                    ),
                                    variant="transparent",
                                    id="tlacidlo-zmena-temy",
                                ),
                            ]
                            + [
                                dmc.MediaQuery(
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="radix-icons:hamburger-menu",
                                            width=25,
                                        ),
                                        variant="transparent",
                                        id="tlacidlo-menu",
                                    ),
                                    largerThan="sm",
                                    styles={"display": "none"},
                                ),
                            ],
                            position="right",
                        ),
                    ],
                    position="apart",
                    style={"margin-right": "2vh", "margin-left": "2vh"},
                ),
                justify="center",
                style={"height": "100%"},
            ),
            dmc.Drawer(
                id="vysuvacie-menu",
                overlayOpacity=0.55,
                overlayBlur=3,
                size=300,
                children=dmc.Stack(
                    [
                        html.A(
                            dmc.NavLink(
                                label=odkazy[link]["label"],
                                href=link,
                                style={
                                    "padding": "7px",
                                    "width": "auto",
                                },
                                styles={
                                    "label": {
                                        "color": "#868E96",
                                        "font-weight": "500",
                                        "font-size": "24px",
                                    },
                                },
                            ),
                            id={
                                "type": "odkaz-menu",
                                "index": link,
                            },
                        )
                        for link in odkazy
                    ],
                    align="center",
                    spacing=5,
                ),
            ),
        ],
        height=40,
        fixed=True,
        style={"margin-bottom": "3px"},
        withBorder=False,
    )


def priprava_dat():
    """Načíta dáta do analýzy a zníži počet kategórií vzdelania."""
    df = pd.read_csv("sldb2021_vzdelani_vek2_pohlavi_iba_kraje.csv")

    vzdelanie_mapovanie = {
        "Bez vzdělání": "Iné",
        "Nezjištěno": "Iné",
        "Neúplné základní vzdělání": "Základné",
        "Nižší střední a střední vzdělání": "SŠ (bez maturity)",
        "Nástavbové vzdělání": "Stredoškolské",
        "Pomaturitní studium": "Stredoškolské",
        "Vysokoškolské bakalářské vzdělání": "Vysokoškolské",
        "Vysokoškolské doktorské vzdělání": "Vysokoškolské",
        "Vysokoškolské magisterské vzdělání": "Vysokoškolské",
        "Vyšší odborné vzdělání": "Stredoškolské",
        "Vyšší odborné vzdělání v konzervatoři": "Stredoškolské",
        "Základní vzdělání": "Základné",
        "Úplné střední odborné vzdělání": "Stredoškolské",
        "Úplné střední všeobecné vzdělání": "Stredoškolské",
    }

    df.replace({"vzdelani_txt": vzdelanie_mapovanie}, inplace=True)
    return df


def stylizuj_graf(fig, theme):
    """Štylizuje plotly bar chart"""
    fig.update_traces(
        marker_color="rgb(207,219,137)",  # Farba jednotlivých stĺpcov
        hovertemplate="%{x}<br>%{y:,.0f} obyvateľov<br>%{customdata[0]:.2%} obyvateľstva",  # Text po priložení myši
    )

    fig.update_layout(
        height=300,  # Výška grafu v pixeloch
        yaxis_title=None,  # Odstráni popis osy y
        xaxis_title=None,  # Odstráni popis osy x
        dragmode=False,  # Vypne inetrakciu s grafom po kliknutí a ťahaní myšou
        bargap=0.4,  # Medzera medzi stĺpacmi
        yaxis=dict(
            gridcolor="whitesmoke"
            if theme == "light"
            else "#484848",  # Farba pomocných čiar mriežky
            gridwidth=0.2,  # Šírka pomocných čiar mriežky
            zeroline=False,  # Vypne pomocnú čiaru z nuly
            color="#444"
            if theme == "light"
            else "#FFFFFF",  # Farba písma popiskov osy y
            nticks=5,  # Počet popiskov na ose y
        ),
        paper_bgcolor="rgba(0, 0, 0, 0)",  # Farba pozadia celej komponenty graf
        font=dict(
            family="Segoe UI",  # Písmo použité v grafe
            size=14,  # Veľkosť písma použitá v grafe
        ),
        margin=dict(r=0, b=10, t=0, l=0),  # Odsadenie grafu od okrajov
        plot_bgcolor="rgba(0, 0, 0, 0)",  # Farba pozadia grafu
        xaxis=dict(
            showgrid=False,  # Vypne pomocné čiary
            zeroline=False,  # Vypne pomocnú čiaru z nuly
            color="#444" if theme == "light" else "#FFFFFF",  # Farba písma na ose x
        ),
    )
    return fig


def ikona_s_odkazom(odkaz, ikona):
    """Vytvorí klikateľnú ikonu, ktorá vedie na externú webovú stránku.

    Parametre:
    odkaz - odkaz na externú webovú stránku
    ikona - názov ikony z knižníc Iconify, ktorá bude použitá ako klikateľné tlačidlo
    """
    return html.A(
        dmc.ActionIcon(
            DashIconify(
                icon=ikona,
                width=30,
            ),
            size="lg",
            variant="transparent",
        ),
        href=odkaz,
        target="_blank",
    )


def gradient_text(text, **kwargs):
    """Vytvorí text štylizovaný gradientom farieb.

    Parametre:
    text - text ktorý sa zvýrazní gradientom
    **kwargs - ostatné keyword argumenty, ktoré sa využijú ako argumenty pre komponentu dmc.Text
    """
    return dmc.Text(
        text,
        variant="gradient",
        gradient={"from": "blue", "to": "teal", "deg": 45},
        **kwargs
    )


def karta_projekt(image, title, description, odkaz):
    """Vytvorí kartu s projektom.

    Parametre:
    image - ilustračný obrázok k projektu
    title - názov projektu
    description - popis projektu
    odkaz - odkaz na podstránku s projektom
    """
    return dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=image,
                    height=160,
                )
            ),
            dmc.Stack(
                [
                    dmc.Text(title, weight=500),
                    dmc.Text(
                        description,
                        size="sm",
                        color="dimmed",
                        style={"height": "65px"},
                    ),
                    dmc.Anchor(
                        dmc.Button(
                            "Navštíviť projekt",
                            variant="light",
                            fullWidth=True,
                            mt="md",
                            radius="md",
                        ),
                        href=odkaz,
                    ),
                ],
                spacing=5,
                mt=5,
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"height": "330px"},
    )


def vytvor_nazov_akordeonu(nazov, logo, popis):
    """Vytvorí hlavičku dmc.Accordion na stránku skúseností.

    Parametre:
    nazov - hlavný popis skúsenosti
    logo - logo skúsenosti
    popis - vedľajší popis skúsenosti
    """
    return dmc.AccordionControl(
        dmc.Grid(
            [
                dmc.Col(
                    [
                        dmc.Avatar(src=logo, radius="xl", size="lg"),
                    ],
                    span="content",
                ),
                dmc.Col(
                    [
                        dmc.Text(nazov),
                        dmc.Text(popis, size="sm", weight=400, color="dimmed"),
                    ],
                    span="auto",
                ),
            ]
        )
    )


def vytvor_obsah_akordeonu(list_s_obsahom):
    """Vytvorí vnútorný obsah dmc.Accordion na stránku skúseností.

    Parametre:
    list_s_obsahom - list z ktorého sa vytvoria odrážky s detailami skúseností
    """
    return dmc.AccordionPanel(
        dmc.List(
            [
                dmc.ListItem(dmc.Text([dmc.Text(obsah, size="sm")]))
                for obsah in list_s_obsahom
            ],
            pl=10,
            pr=30,
            pb=10,
        )
    )


def vytvor_akordeon(data_pre_akordeon):
    """Vytvorí list prvkov pre dmc.Accordion na stránku skúseností.

    Parametre:
    data_pre_akordeon - list so slovníkmi skúseností ktoré majú prvky: id, logo, nazov, popis a obsah, ktorý obsahuje
    list
    """
    return [
        dmc.AccordionItem(
            [
                vytvor_nazov_akordeonu(
                    jedna_polozka["nazov"],
                    jedna_polozka["logo"],
                    jedna_polozka["popis"],
                ),
                vytvor_obsah_akordeonu(jedna_polozka["obsah"]),
            ],
            value=jedna_polozka["id"],
        )
        for jedna_polozka in data_pre_akordeon
    ]
