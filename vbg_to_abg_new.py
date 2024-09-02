import pandas as pd

# Conversion functions based on typical regression approximations
def abg_to_vbg_pH(abg_pH):
    return (abg_pH - 0.42) / 0.95

def abg_to_vbg_pCO2(abg_pCO2):
    return (abg_pCO2 - 0.19) / 0.9

def abg_to_vbg_pO2(abg_pO2):
    return (abg_pO2 - 5) / 1.1

def abg_to_vbg_sO2(abg_sO2):
    return (abg_sO2 - 2.3) / 0.98

def abg_to_vbg_Hct(abg_Hct):
    return (abg_Hct - 2.1) / 0.88

def abg_to_vbg_tHb(abg_tHb):
    return (abg_tHb - 0.5) / 0.9

def abg_to_vbg_sodium(abg_sodium):
    return (abg_sodium - 14.44) / 0.9

def abg_to_vbg_potassium(abg_potassium):
    return (abg_potassium - 0.34) / 0.91

def abg_to_vbg_ionizedCa(abg_ionizedCa):
    return (abg_ionizedCa - 0.29) / 0.7

def abg_to_vbg_ionizedMg(abg_ionizedMg):
    return (abg_ionizedMg - 0.12) / 0.8

def abg_to_vbg_glucose(abg_glucose):
    return (abg_glucose - 5) / 1.1

def abg_to_vbg_lactate(abg_lactate):
    return (abg_lactate - 0.12) / 0.92

def abg_to_vbg_O2Hb(abg_O2Hb):
    return (abg_O2Hb - 1) / 0.95

def abg_to_vbg_CoHb(abg_CoHb):
    return (abg_CoHb - 0.5) / 0.9

def abg_to_vbg_MetHb(abg_MetHb):
    return (abg_MetHb - 0.2) / 0.85

def abg_to_vbg_HHb(abg_HHb):
    return (abg_HHb - 0.7) / 0.92

def abg_to_vbg_tBil(abg_tBil):
    return (abg_tBil - 0.05) / 0.9

def abg_to_vbg_HbF(abg_HbF):
    return (abg_HbF - 0.1) / 0.88

def abg_to_vbg_tCO2(abg_tCO2):
    return (abg_tCO2 - 1.5) / 0.9

# Load ABG data from Excel
input_file = 'abg_data.xlsx'
abg_data = pd.read_excel(input_file)

# Initialize a DataFrame for VBG data
vbg_data = pd.DataFrame()

# Apply conversion functions
vbg_data['VBG pH'] = abg_data['ABG pH'].apply(abg_to_vbg_pH)
vbg_data['VBG pCO2 (mmHg)'] = abg_data['ABG pCO2 (mmHg)'].apply(abg_to_vbg_pCO2)
vbg_data['VBG pO2 (mmHg)'] = abg_data['ABG pO2 (mmHg)'].apply(abg_to_vbg_pO2)
vbg_data['VBG sO2 (%)'] = abg_data['ABG sO2 (%)'].apply(abg_to_vbg_sO2)
vbg_data['VBG Hct (%)'] = abg_data['ABG Hct (%)'].apply(abg_to_vbg_Hct)
vbg_data['VBG tHb (g/dL)'] = abg_data['ABG tHb (g/dL)'].apply(abg_to_vbg_tHb)
vbg_data['VBG S. Sodium (mmol/L)'] = abg_data['ABG S. Sodium (mmol/L)'].apply(abg_to_vbg_sodium)
vbg_data['VBG S. Potassium (mmol/L)'] = abg_data['ABG S. Potassium (mmol/L)'].apply(abg_to_vbg_potassium)
vbg_data['VBG Ionized Ca2+ (mmol/L)'] = abg_data['ABG Ionized Ca2+ (mmol/L)'].apply(abg_to_vbg_ionizedCa)
vbg_data['VBG Ionized Mg2+ (mmol/L)'] = abg_data['ABG Ionized Mg2+ (mmol/L)'].apply(abg_to_vbg_ionizedMg)
vbg_data['VBG Glucose (mg/dL)'] = abg_data['ABG Glucose (mg/dL)'].apply(abg_to_vbg_glucose)
vbg_data['VBG Lactate (mmol/L)'] = abg_data['ABG Lactate (mmol/L)'].apply(abg_to_vbg_lactate)
vbg_data['VBG O2Hb (%)'] = abg_data['ABG O2Hb (%)'].apply(abg_to_vbg_O2Hb)
vbg_data['VBG CoHb (%)'] = abg_data['ABG CoHb (%)'].apply(abg_to_vbg_CoHb)
vbg_data['VBG MetHb (%)'] = abg_data['ABG MetHb (%)'].apply(abg_to_vbg_MetHb)
vbg_data['VBG HHb (%)'] = abg_data['ABG HHb (%)'].apply(abg_to_vbg_HHb)
vbg_data['VBG tBil (mg/dL)'] = abg_data['ABG tBil (mg/dL)'].apply(abg_to_vbg_tBil)
vbg_data['VBG HbF (%)'] = abg_data['ABG HbF (%)'].apply(abg_to_vbg_HbF)
vbg_data['VBG tCO2 (mmol/L)'] = abg_data['ABG tCO2 (mmol/L)'].apply(abg_to_vbg_tCO2)

# Save VBG data to Excel
output_file = 'vbg_data.xlsx'
vbg_data.to_excel(output_file, index=False)

print(f"VBG data has been successfully saved to {output_file}.")
