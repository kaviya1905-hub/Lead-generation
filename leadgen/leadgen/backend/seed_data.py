from models import insert_company

# ---------------------------------------------------------
# 1. CEO → Fintech Companies
# ---------------------------------------------------------
fintech_ceo = [
("Razorpay","Bangalore","India"),("Paytm","Noida","India"),("PhonePe","Bangalore","India"),
("Cred","Bangalore","India"),("BharatPe","Delhi","India"),("Slice","Bangalore","India"),
("MobiKwik","Gurgaon","India"),("Pine Labs","Noida","India"),("Juspay","Bangalore","India"),
("Groww","Bangalore","India"),("Zerodha","Bangalore","India"),("Niyo","Bangalore","India"),
("MoneyTap","Bangalore","India"),("Cashfree","Bangalore","India"),("PolicyBazaar","Gurgaon","India"),
("Upstox","Mumbai","India"),("LendingKart","Ahmedabad","India"),("Kissht","Mumbai","India"),
("ETMoney","Delhi","India"),("Revolut","London","UK")
]
for c in fintech_ceo:
    insert_company(c[0],c[1],c[2],"CEO","Fintech")


# ---------------------------------------------------------
# 2. Clinic Owner → Dental Clinics
# ---------------------------------------------------------
dental_clinic = [
("Clove Dental","Delhi","India"),("Sabka Dentist","Mumbai","India"),("Partha Dental","Hyderabad","India"),
("Apollo Dental","Chennai","India"),("Smile Care","Pune","India"),("Dentics Care","Bangalore","India"),
("ToothCraft Dental","Bangalore","India"),("White Dental Studio","Hyderabad","India"),("The Dental Lounge","Delhi","India"),
("Healthy Smile Dental","Kolkata","India"),("Bright Dental Care","Jaipur","India"),("Perfect 32 Dental","Ahmedabad","India"),
("Smile Point","Chandigarh","India"),("Prime Dental","Surat","India"),("Shine Dental Hub","Indore","India"),
("Dental Roots","Gurgaon","India"),("Studio 32 Dental","Bangalore","India"),("Pearl Dental","Mumbai","India"),
("Cosmo Dental Clinic","Delhi","India"),("Happy Teeth Dental","Chennai","India")
]
for c in dental_clinic:
    insert_company(c[0],c[1],c[2],"Clinic Owner","Dental Clinic")


# ---------------------------------------------------------
# 3. HR Manager → IT/Corporate
# ---------------------------------------------------------
hr_it = [
("Infosys","Bangalore","India"),("Wipro","Bangalore","India"),("TCS","Mumbai","India"),
("HCL","Noida","India"),("Tech Mahindra","Pune","India"),("Accenture","Bangalore","India"),
("Cognizant","Chennai","India"),("Capgemini","Mumbai","India"),("IBM India","Bangalore","India"),
("Mindtree","Bangalore","India"),("Oracle India","Bangalore","India"),("DXC Technology","Bangalore","India"),
("LTI Mindtree","Mumbai","India"),("SAP Labs","Bangalore","India"),("Persistent Systems","Pune","India"),
("Mphasis","Bangalore","India"),("Zoho","Chennai","India"),("Adobe India","Noida","India")
]
for c in hr_it:
    insert_company(c[0],c[1],c[2],"HR Manager","IT/Corporate")


# ---------------------------------------------------------
# 4. Operations Manager → Manufacturing Industry
# ---------------------------------------------------------
operations_manufacturing = [
("Tata Steel","Jamshedpur","India"),("Bosch Limited","Bangalore","India"),("L&T","Mumbai","India"),
("JSW Steel","Mumbai","India"),("Aditya Birla Group","Mumbai","India"),("Reliance Industries","Mumbai","India"),
("Hindalco","Mumbai","India"),("Bharat Forge","Pune","India"),("Ashok Leyland","Chennai","India"),
("Mahindra & Mahindra","Mumbai","India"),("Tata Motors","Pune","India"),("Maruti Suzuki","Delhi","India"),
("TVS Motors","Chennai","India"),("Bajaj Auto","Pune","India"),("Schneider Electric","Bangalore","India"),
("Siemens India","Mumbai","India"),("Jindal Steel","Delhi","India"),("Amara Raja","Tirupati","India")
]
for c in operations_manufacturing:
    insert_company(c[0],c[1],c[2],"Operations Manager","Manufacturing")


# ---------------------------------------------------------
# 5. Founder / Startup Owner → SaaS/Tech
# ---------------------------------------------------------
startup_saas = [
("Freshworks","Chennai","India"),("Zoho","Chennai","India"),("Chargebee","Chennai","India"),
("Postman","Bangalore","India"),("BrowserStack","Mumbai","India"),("Unacademy","Bangalore","India"),
("Byju's","Bangalore","India"),("CRED","Bangalore","India"),("Agara Labs","Bangalore","India"),
("Locus","Bangalore","India"),("Rapido","Bangalore","India"),("ShareChat","Bangalore","India"),
("InMobi","Bangalore","India"),("Swiggy","Bangalore","India"),("Zomato","Gurgaon","India"),
("Ola","Bangalore","India"),("Meesho","Bangalore","India"),("Quora","California","USA")
]
for c in startup_saas:
    insert_company(c[0],c[1],c[2],"Founder","SaaS/Tech")


# ---------------------------------------------------------
# 6. E-commerce Manager → Online Retail
# ---------------------------------------------------------
ecommerce = [
("Flipkart","Bangalore","India"),("Amazon","Bangalore","India"),("Myntra","Bangalore","India"),
("Ajio","Bangalore","India"),("Nykaa","Mumbai","India"),("Tata Cliq","Mumbai","India"),
("Pepperfry","Mumbai","India"),("BigBasket","Bangalore","India"),("Blinkit","Gurgaon","India"),
("Zivame","Bangalore","India"),("Lenskart","Delhi","India"),("FirstCry","Pune","India"),
("Paytm Mall","Noida","India"),("ShopClues","Gurgaon","India"),("Urban Ladder","Bangalore","India"),
("Reliance Trends","Mumbai","India"),("DMart","Mumbai","India"),("JioMart","Mumbai","India")
]
for c in ecommerce:
    insert_company(c[0],c[1],c[2],"E-commerce Manager","Online Retail")


# ---------------------------------------------------------
# 7. Hospital Administrator → Multi-speciality Hospitals
# ---------------------------------------------------------
hospital_admin = [
("Apollo Hospitals","Chennai","India"),("Fortis Healthcare","Delhi","India"),("Max Hospitals","Delhi","India"),
("Manipal Hospitals","Bangalore","India"),("Narayana Health","Bangalore","India"),("Aster Hospitals","Dubai","UAE"),
("Global Hospitals","Chennai","India"),("KIMS Hospital","Hyderabad","India"),("Medanta","Gurgaon","India"),
("Columbia Asia","Bangalore","India"),("Care Hospitals","Hyderabad","India"),("Sunshine Hospitals","Hyderabad","India"),
("AMRI Hospitals","Kolkata","India"),("Rainbow Hospitals","Hyderabad","India"),("Vijaya Hospital","Chennai","India"),
("SevenHills Hospital","Mumbai","India"),("Lilavati Hospital","Mumbai","India"),("Hiranandani Hospitals","Mumbai","India")
]
for c in hospital_admin:
    insert_company(c[0],c[1],c[2],"Hospital Administrator","Multispeciality Hospital")

# ---------------------------------------------------------
# 8. Real Estate Developer → Construction & Realty
# ---------------------------------------------------------
real_estate = [
("DLF","Delhi","India"),("Brigade Group","Bangalore","India"),("Lodha Group","Mumbai","India"),
("Prestige Group","Bangalore","India"),("Sobha Developers","Bangalore","India"),("Godrej Properties","Mumbai","India"),
("Hiranandani Group","Mumbai","India"),("Puravankara","Bangalore","India"),("Oberoi Realty","Mumbai","India"),
("Tata Housing","Mumbai","India"),("Mahindra Lifespaces","Mumbai","India"),("Raheja Developers","Delhi","India"),
("NoBrokerHood","Bangalore","India"),("Embassy Group","Bangalore","India"),("Phoenix Mills","Mumbai","India")
]
for c in real_estate:
    insert_company(c[0],c[1],c[2],"Real Estate Developer","Construction & Realty")


# ---------------------------------------------------------
# 9. School Principal → Educational Institutions
# ---------------------------------------------------------
schools = [
("Delhi Public School","Delhi","India"),("Ryan International","Mumbai","India"),("DAV Public School","Delhi","India"),
("Kendriya Vidyalaya","Delhi","India"),("VIBGYOR High","Mumbai","India"),("Orchids International","Bangalore","India"),
("National Public School","Bangalore","India"),("EuroSchool","Mumbai","India"),("Chinmaya Vidyalaya","Chennai","India"),
("Vidya Mandir","Chennai","India"),("Amity International","Gurgaon","India"),("Velammal School","Chennai","India"),
("PSBB School","Chennai","India"),("The Indian Public School","Coimbatore","India"),("Greenwood High","Bangalore","India")
]
for c in schools:
    insert_company(c[0],c[1],c[2],"School Principal","Educational Institution")


# ---------------------------------------------------------
# 10. Restaurant Owner → Food & Hospitality
# ---------------------------------------------------------
restaurants = [
("McDonald's","Multiple","India"),("KFC","Multiple","India"),("Domino's","Multiple","India"),
("Burger King","Multiple","India"),("Subway","Multiple","India"),("Barbeque Nation","Multiple","India"),
("Mainland China","Kolkata","India"),("Cream Stone","Hyderabad","India"),("Theobroma","Mumbai","India"),
("Faasos","Pune","India"),("EatFit","Bangalore","India"),("Chai Point","Bangalore","India"),
("Bikanervala","Delhi","India"),("Haldiram's","Delhi","India"),("Wow Momo","Kolkata","India")
]
for c in restaurants:
    insert_company(c[0],c[1],c[2],"Restaurant Owner","Food & Hospitality")


# ---------------------------------------------------------
# 11. Logistics Head → Supply Chain & Warehouse
# ---------------------------------------------------------
logistics = [
("DHL","Mumbai","India"),("Blue Dart","Mumbai","India"),("DTDC","Bangalore","India"),
("Delhivery","Gurgaon","India"),("GATI","Hyderabad","India"),("Ecom Express","Delhi","India"),
("FedEx India","Mumbai","India"),("Amazon Logistics","Bangalore","India"),("XpressBees","Pune","India"),
("Shadowfax","Bangalore","India"),("Porter","Bangalore","India"),("TurtleMint Logistics","Mumbai","India"),
("TCI Express","Gurgaon","India"),("Mahindra Logistics","Mumbai","India"),("Safexpress","Delhi","India")
]
for c in logistics:
    insert_company(c[0],c[1],c[2],"Logistics Head","Supply Chain")


# ---------------------------------------------------------
# 12. Sales Manager → B2B / SaaS
# ---------------------------------------------------------
sales_saas = [
("Salesforce","California","USA"),("HubSpot","Massachusetts","USA"),("Freshsales","Chennai","India"),
("Zoho CRM","Chennai","India"),("LeadSquared","Bangalore","India"),("Pipedrive","USA","Global"),
("Outreach","USA","Global"),("Apollo.io","USA","Global"),("LinkedIn Sales","USA","Global"),
("Close CRM","USA","Global"),("Intercom","USA","Global"),("Slack","USA","Global"),
("Notion","USA","Global"),("Asana","USA","Global"),("Monday.com","USA","Global")
]
for c in sales_saas:
    insert_company(c[0],c[1],c[2],"Sales Manager","B2B/SaaS")


# ---------------------------------------------------------
# 13. Product Manager → SaaS & Software
# ---------------------------------------------------------
product_saas = [
("Figma","USA","Global"),("Atlassian","USA","Global"),("Notion","USA","Global"),
("Microsoft","USA","Global"),("Google","USA","Global"),("Adobe","USA","Global"),
("Freshworks","Chennai","India"),("Zoho","Chennai","India"),("BrowserStack","Mumbai","India"),
("Postman","Bangalore","India"),("Jira (Atlassian)","USA","Global"),("Slack","USA","Global"),
("GitHub","USA","Global"),("Datadog","USA","Global"),("Twilio","USA","Global")
]
for c in product_saas:
    insert_company(c[0],c[1],c[2],"Product Manager","SaaS & Software")


# ---------------------------------------------------------
# 14. Finance Manager → Banking/NBFC
# ---------------------------------------------------------
banking_finance = [
("HDFC Bank","Mumbai","India"),("ICICI Bank","Mumbai","India"),("SBI","Mumbai","India"),
("Axis Bank","Mumbai","India"),("Kotak Mahindra Bank","Mumbai","India"),("Yes Bank","Mumbai","India"),
("IDFC First Bank","Mumbai","India"),("IndusInd Bank","Mumbai","India"),("Federal Bank","Kerala","India"),
("Bajaj Finserv","Pune","India"),("Tata Capital","Mumbai","India"),("Muthoot Finance","Kerala","India"),
("Mahindra Finance","Mumbai","India"),("LIC Housing Finance","Mumbai","India"),("Shriram Finance","Chennai","India")
]
for c in banking_finance:
    insert_company(c[0],c[1],c[2],"Finance Manager","Banking/NBFC")


# ---------------------------------------------------------
# 15. Procurement Head → Manufacturing
# ---------------------------------------------------------
procurement_manufacturing = [
("L&T","Mumbai","India"),("Bharat Forge","Pune","India"),("Tata Steel","Jamshedpur","India"),
("JSW Steel","Mumbai","India"),("Bosch","Bangalore","India"),("Mahindra","Mumbai","India"),
("Hyundai India","Chennai","India"),("Maruti Suzuki","Delhi","India"),("Siemens India","Mumbai","India"),
("Schneider Electric","Bangalore","India"),("Vedanta","Delhi","India"),("Jindal Steel","Delhi","India"),
("UltraTech Cement","Mumbai","India"),("Adani Group","Ahmedabad","India"),("Reliance Industries","Mumbai","India")
]
for c in procurement_manufacturing:
    insert_company(c[0],c[1],c[2],"Procurement Head","Manufacturing")


# ---------------------------------------------------------
# 16. Gym/Fitness Studio Owner → Fitness
# ---------------------------------------------------------
fitness = [
("CultFit","Bangalore","India"),("Gold's Gym","Mumbai","India"),("Anytime Fitness","Delhi","India"),
("Talwalkars","Mumbai","India"),("Powerhouse Gym","Mumbai","India"),("Snap Fitness","Bangalore","India"),
("Fit7 by MS Dhoni","Delhi","India"),("Plus Fitness","Mumbai","India"),("Chisel Fitness","Bangalore","India"),
("BodyPower Gym","Mumbai","India"),("MultiFit","Pune","India"),("Skulpt Gym","Pune","India"),
("Transform Gym","Mumbai","India"),("BodyZone Gym","Chandigarh","India"),("Fitness First","Delhi","India")
]
for c in fitness:
    insert_company(c[0],c[1],c[2],"Gym Owner","Fitness")


# ---------------------------------------------------------
# 17. Hotel Manager → Hospitality (Hotels)
# ---------------------------------------------------------
hotels = [
("Taj Hotels","Mumbai","India"),("Marriott","Bangalore","India"),("ITC Hotels","Delhi","India"),
("Hyatt","Mumbai","India"),("Hilton","Bangalore","India"),("The Leela","Mumbai","India"),
("Radisson Blu","Delhi","India"),("Oberoi Hotels","Mumbai","India"),("Novotel","Hyderabad","India"),
("Holiday Inn","Mumbai","India"),("JW Marriott","Mumbai","India"),("Trident Hotels","Mumbai","India"),
("Ginger Hotels","Mumbai","India"),("The Park Hotels","Chennai","India"),("The Lalit","Delhi","India")
]
for c in hotels:
    insert_company(c[0],c[1],c[2],"Hotel Manager","Hospitality")


print("\n===================================================")
print("Backend identified Successfully!")
print("===================================================\n")
