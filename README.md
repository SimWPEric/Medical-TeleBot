# CAD Medical Screening

CAD (Coronary Artery Disease) medical screening Telegram Bot helps healthcare professionals make decisions based on a set of input parameters. The tool evaluates various symptoms, risk factors, recent test results, and provides a final decision based on these inputs.

## Inputs

The screening tool takes the following inputs:

### Symptoms
- [ ] FALSE
- [ ] Shortness of Breath (SOB)
- [ ] Chest pain

### PVD/CVA/FH (Peripheral Vascular Disease / Cerebrovascular Accident / Family History)
- [ ] FALSE
- [ ] TRUE

### RECENT TEST (Recent Medical Test Results)
- [ ] NEGATIVE
- [ ] Not Applicable (N/A)
- [ ] SUGGESTIVE

### Risk Factors

#### RF: FHX PREM (Family History of Premature CAD)
- [ ] FALSE
- [ ] TRUE

#### RF: CKD (Chronic Kidney Disease)
- [ ] FALSE
- [ ] Very high risk or high risk
- [ ] Diabetes Mellitus (DM)

#### RF: DM (Diabetes Mellitus)
- [ ] FALSE
- [ ] Moderate risk
- [ ] Very high risk or high risk

#### RF: Others (ACC 2019)
- [ ] FALSE
- [ ] TRUE

### Scoring

#### FHS TYR (Framingham Heart Study 10-Year Risk)
- [ ] LOW
- [ ] INTERMEDIATE (INT)
- [ ] HIGH

### Decision

The tool will provide one of the following final decisions based on the inputs:

- [ ] RF Management (Risk Factor Management)
- [ ] Functional or Anatomical Assessment
- [ ] Exercise ECG (Electrocardiogram)
- [ ] Not Applicable
- [ ] Coronary Artery Calcium (Ca) Score
- [ ] Symptomatic: Diamond Forrester Score (ESC 2019)

## Output

The final decision from this CAD medical screening tool is based on the combination of answers to these 8 questions. It provides a recommendation for further medical evaluation or management based on the individual's risk factors and symptoms.

## Usage

To use this CAD medical screening tool:

1. Select the appropriate options for each input category based on the patient's information.

2. Once all inputs are selected, run the tool to obtain the final decision.

Please note that this tool is intended for use by healthcare professionals and should not replace a comprehensive medical evaluation.
