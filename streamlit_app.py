#program with the use of Dictionary
"""- - - This program firstly ask that where are you from then according to
your country they provide code of your country for entering our
mobile phone number- - -"""
import streamlit as st

def phone():
    country_code = {
    "AFG": "+93",
    "ALB": "+355",
    "DZA": "+213",
    "AND": "+376",
    "AGO": "+244",
    "ATG": "+1-268",
    "ARG": "+54",
    "ARM": "+374",
    "AUS": "+61",
    "AUT": "+43",
    "AZE": "+994",

    "BHS": "+1-242",
    "BHR": "+973",
    "BGD": "+880",
    "BRB": "+1-246",
    "BLR": "+375",
    "BEL": "+32",
    "BLZ": "+501",
    "BEN": "+229",
    "BTN": "+975",
    "BOL": "+591",
    "BIH": "+387",
    "BWA": "+267",
    "BRA": "+55",
    "BRN": "+673",
    "BGR": "+359",
    "BFA": "+226",
    "BDI": "+257",

    "KHM": "+855",
    "CMR": "+237",
    "CAN": "+1",
    "CPV": "+238",
    "CAF": "+236",
    "TCD": "+235",
    "CHL": "+56",
    "CHN": "+86",
    "COL": "+57",
    "COM": "+269",
    "COG": "+242",
    "CRI": "+506",
    "HRV": "+385",
    "CUB": "+53",
    "CYP": "+357",
    "CZE": "+420",

    "DNK": "+45",
    "DJI": "+253",
    "DMA": "+1-767",
    "DOM": "+1-809",

    "ECU": "+593",
    "EGY": "+20",
    "SLV": "+503",
    "GNQ": "+240",
    "ERI": "+291",
    "EST": "+372",
    "SWZ": "+268",
    "ETH": "+251",

    "FJI": "+679",
    "FIN": "+358",
    "FRA": "+33",

    "GAB": "+241",
    "GMB": "+220",
    "GEO": "+995",
    "DEU": "+49",
    "GHA": "+233",
    "GRC": "+30",
    "GRD": "+1-473",
    "GTM": "+502",
    "GIN": "+224",
    "GNB": "+245",
    "GUY": "+592",

    "HTI": "+509",
    "HND": "+504",
    "HUN": "+36",

    "ISL": "+354",
    "IND": "+91",
    "IDN": "+62",
    "IRN": "+98",
    "IRQ": "+964",
    "IRL": "+353",
    "ISR": "+972",
    "ITA": "+39",

    "JAM": "+1-876",
    "JPN": "+81",
    "JOR": "+962",

    "KAZ": "+7",
    "KEN": "+254",
    "KIR": "+686",
    "PRK": "+850",
    "KOR": "+82",
    "KWT": "+965",
    "KGZ": "+996",

    "LAO": "+856",
    "LVA": "+371",
    "LBN": "+961",
    "LSO": "+266",
    "LBR": "+231",
    "LBY": "+218",
    "LIE": "+423",
    "LTU": "+370",
    "LUX": "+352",

    "MDG": "+261",
    "MWI": "+265",
    "MYS": "+60",
    "MDV": "+960",
    "MLI": "+223",
    "MLT": "+356",
    "MHL": "+692",
    "MRT": "+222",
    "MUS": "+230",
    "MEX": "+52",
    "FSM": "+691",
    "MDA": "+373",
    "MCO": "+377",
    "MNG": "+976",
    "MNE": "+382",
    "MAR": "+212",
    "MOZ": "+258",
    "MMR": "+95",

    "NAM": "+264",
    "NRU": "+674",
    "NPL": "+977",
    "NLD": "+31",
    "NZL": "+64",
    "NIC": "+505",
    "NER": "+227",
    "NGA": "+234",
    "MKD": "+389",
    "NOR": "+47",

    "OMN": "+968",

    "PAK": "+92",
    "PLW": "+680",
    "PAN": "+507",
    "PNG": "+675",
    "PRY": "+595",
    "PER": "+51",
    "PHL": "+63",
    "POL": "+48",
    "PRT": "+351",

    "QAT": "+974",

    "ROU": "+40",
    "RUS": "+7",
    "RWA": "+250",

    "KSA": "+966",
    "SEN": "+221",
    "SRB": "+381",
    "SYC": "+248",
    "SLE": "+232",
    "SGP": "+65",
    "SVK": "+421",
    "SVN": "+386",
    "SLB": "+677",
    "SOM": "+252",
    "ZAF": "+27",
    "ESP": "+34",
    "LKA": "+94",
    "SDN": "+249",
    "SUR": "+597",
    "SWE": "+46",
    "CHE": "+41",
    "SYR": "+963",

    "TWN": "+886",
    "TJK": "+992",
    "TZA": "+255",
    "THA": "+66",
    "TLS": "+670",
    "TGO": "+228",
    "TON": "+676",
    "TTO": "+1-868",
    "TUN": "+216",
    "TUR": "+90",
    "TKM": "+993",
    "TUV": "+688",

    "UGA": "+256",
    "UKR": "+380",
    "ARE": "+971",
    "GBR": "+44",
    "USA": "+1",
    "URY": "+598",
    "UZB": "+998",

    "VUT": "+678",
    "VAT": "+379",
    "VEN": "+58",
    "VNM": "+84",

    "YEM": "+967",
    "ZMB": "+260",
    "ZWE": "+263"}
    st.title("📱 Country Phone Code Finder")

    st.write("Enter **first 3-letter country code in CAPITAL** (e.g. IND, USA, GBR)")

    country = st.text_input("Country Code")
    mobile = st.text_input("Mobile Number")

    if st.button("Continue"):
        if country == "" or mobile == "":
            st.error("Please fill all fields ❌")
        elif country not in country_code:
            st.error("Invalid country code ❌")
        else:
            st.balloons()
            code = country_code[country]
            st.success("Phone Number Generated ✅")
            st.write(f"📞 **{code} {mobile}**")

phone()

