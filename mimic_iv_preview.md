# MIMIC-IV v2.2 数据集预览（每表前5行）

## `hosp/` 目录

### `hosp/admissions.csv.gz`

| subject_id | hadm_id | admittime | dischtime | deathtime | admission_type | admit_provider_id | admission_location | discharge_location | insurance | language | marital_status | race | edregtime | edouttime | hospital_expire_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 2180-05-06 22:23:00 | 2180-05-07 17:15:00 |  | URGENT | P874LG | TRANSFER FROM HOSPITAL | HOME | Other | ENGLISH | WIDOWED | WHITE | 2180-05-06 19:17:00 | 2180-05-06 23:30:00 | 0 |
| 10000032 | 22841357 | 2180-06-26 18:27:00 | 2180-06-27 18:49:00 |  | EW EMER. | P09Q6Y | EMERGENCY ROOM | HOME | Medicaid | ENGLISH | WIDOWED | WHITE | 2180-06-26 15:54:00 | 2180-06-26 21:31:00 | 0 |
| 10000032 | 25742920 | 2180-08-05 23:44:00 | 2180-08-07 17:50:00 |  | EW EMER. | P60CC5 | EMERGENCY ROOM | HOSPICE | Medicaid | ENGLISH | WIDOWED | WHITE | 2180-08-05 20:58:00 | 2180-08-06 01:44:00 | 0 |
| 10000032 | 29079034 | 2180-07-23 12:35:00 | 2180-07-25 17:55:00 |  | EW EMER. | P30KEH | EMERGENCY ROOM | HOME | Medicaid | ENGLISH | WIDOWED | WHITE | 2180-07-23 05:54:00 | 2180-07-23 14:00:00 | 0 |
| 10000068 | 25022803 | 2160-03-03 23:16:00 | 2160-03-04 06:26:00 |  | EU OBSERVATION | P51VDL | EMERGENCY ROOM |  | Other | ENGLISH | SINGLE | WHITE | 2160-03-03 21:55:00 | 2160-03-04 06:26:00 | 0 |

### `hosp/d_hcpcs.csv.gz`

| code | category | long_description | short_description |
| --- | --- | --- | --- |
| 00000 |  |  | Invalid Code |
| 0001F | 2.0 |  | Composite measures |
| 0002F | 2.0 |  | Composite measures |
| 0003F | 2.0 |  | Composite measures |
| 0004F | 2.0 |  | Composite measures |

### `hosp/d_icd_diagnoses.csv.gz`

| icd_code | icd_version | long_title |
| --- | --- | --- |
| 10 | 9 | Cholera due to vibrio cholerae |
| 11 | 9 | Cholera due to vibrio cholerae el tor |
| 19 | 9 | Cholera, unspecified |
| 20 | 9 | Typhoid fever |
| 21 | 9 | Paratyphoid fever A |

### `hosp/d_icd_procedures.csv.gz`

| icd_code | icd_version | long_title |
| --- | --- | --- |
| 1 | 9 | Therapeutic ultrasound of vessels of head and neck |
| 2 | 9 | Therapeutic ultrasound of heart |
| 3 | 9 | Therapeutic ultrasound of peripheral vascular vessels |
| 9 | 9 | Other therapeutic ultrasound |
| 1 | 10 | Central Nervous System and Cranial Nerves, Bypass |

### `hosp/d_labitems.csv.gz`

| itemid | label | fluid | category |
| --- | --- | --- | --- |
| 50801 | Alveolar-arterial Gradient | Blood | Blood Gas |
| 50802 | Base Excess | Blood | Blood Gas |
| 50803 | Calculated Bicarbonate, Whole Blood | Blood | Blood Gas |
| 50804 | Calculated Total CO2 | Blood | Blood Gas |
| 50805 | Carboxyhemoglobin | Blood | Blood Gas |

### `hosp/diagnoses_icd.csv.gz`

| subject_id | hadm_id | seq_num | icd_code | icd_version |
| --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 1 | 5723 | 9 |
| 10000032 | 22595853 | 2 | 78959 | 9 |
| 10000032 | 22595853 | 3 | 5715 | 9 |
| 10000032 | 22595853 | 4 | 7070 | 9 |
| 10000032 | 22595853 | 5 | 496 | 9 |

### `hosp/drgcodes.csv.gz`

| subject_id | hadm_id | drg_type | drg_code | description | drg_severity | drg_mortality |
| --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | APR | 283 | OTHER DISORDERS OF THE LIVER | 2.0 | 2.0 |
| 10000032 | 22595853 | HCFA | 442 | DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W CC |  |  |
| 10000032 | 22841357 | APR | 279 | HEPATIC COMA & OTHER MAJOR ACUTE LIVER DISORDERS | 3.0 | 2.0 |
| 10000032 | 22841357 | HCFA | 442 | DISORDERS OF LIVER EXCEPT MALIG,CIRR,ALC HEPA W CC |  |  |
| 10000032 | 25742920 | APR | 283 | OTHER DISORDERS OF THE LIVER | 3.0 | 2.0 |

### `hosp/emar.csv.gz`

| subject_id | hadm_id | emar_id | emar_seq | poe_id | pharmacy_id | enter_provider_id | charttime | medication | event_txt | scheduletime | storetime |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 10000032-10 | 10 | 10000032-36 | 48770010 |  | 2180-05-07 00:44:00 | Potassium Chloride | Administered | 2180-05-07 00:44:00 | 2180-05-07 00:44:00 |
| 10000032 | 22595853 | 10000032-11 | 11 | 10000032-22 | 14779570 |  | 2180-05-07 00:44:00 | Sodium Chloride 0.9%  Flush | Flushed | 2180-05-07 00:44:00 | 2180-05-07 00:44:00 |
| 10000032 | 22595853 | 10000032-12 | 12 | 10000032-37 | 93463122 |  | 2180-05-07 06:10:00 | Ipratropium Bromide Neb | Administered | 2180-05-07 06:00:00 | 2180-05-07 06:10:00 |
| 10000032 | 22595853 | 10000032-13 | 13 | 10000032-28 | 42497745 |  | 2180-05-07 05:00:00 | Albuterol Inhaler | Administered | 2180-05-07 06:29:00 | 2180-05-07 06:29:00 |
| 10000032 | 22595853 | 10000032-14 | 14 | 10000032-29 | 69131933 |  | 2180-05-07 07:51:00 | Emtricitabine-Tenofovir (Truvada) | Administered | 2180-05-07 08:00:00 | 2180-05-07 07:56:00 |

### `hosp/emar_detail.csv.gz`

| subject_id | emar_id | emar_seq | parent_field_ordinal | administration_type | pharmacy_id | barcode_type | reason_for_no_barcode | complete_dose_not_given | dose_due | dose_due_unit | dose_given | dose_given_unit | will_remainder_of_dose_be_given | product_amount_given | product_unit | product_code | product_description | product_description_other | prior_infusion_rate | infusion_rate | infusion_rate_adjustment | infusion_rate_adjustment_amount | infusion_rate_unit | route | infusion_complete | completion_interval | new_iv_bag_hung | continued_infusion_in_other_location | restart_interval | side | site | non_formulary_visual_verification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 10000032-10 | 10 | 1.1 |  | 48770010.0 | if |  |  |  |  | 10.0 | mEq |  | 1.0 | TAB | MICROK10 | Potassium Chloride 10mEq ER Tablet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10000032 | 10000032-10 | 10 | 1.2 |  | 48770010.0 | if |  |  |  |  | 10.0 | mEq |  | 1.0 | TAB | MICROK10 | Potassium Chloride 10mEq ER Tablet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10000032 | 10000032-10 | 10 | 1.3 |  | 48770010.0 | if |  |  |  |  | 10.0 | mEq |  | 1.0 | TAB | MICROK10 | Potassium Chloride 10mEq ER Tablet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10000032 | 10000032-10 | 10 | 1.4 |  | 48770010.0 | if |  |  |  |  | 10.0 | mEq |  | 1.0 | TAB | MICROK10 | Potassium Chloride 10mEq ER Tablet |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10000032 | 10000032-10 | 10 |  | Standard Maintenance Medication |  |  |  | No | 40.0 | mEq |  |  | No |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### `hosp/hcpcsevents.csv.gz`

| subject_id | hadm_id | chartdate | hcpcs_cd | seq_num | short_description |
| --- | --- | --- | --- | --- | --- |
| 10000068 | 25022803 | 2160-03-04 | 99218 | 1 | Hospital observation services |
| 10000084 | 29888819 | 2160-12-28 | G0378 | 1 | Hospital observation per hr |
| 10000108 | 27250926 | 2163-09-27 | 99219 | 1 | Hospital observation services |
| 10000117 | 22927623 | 2181-11-15 | 43239 | 1 | Digestive system |
| 10000117 | 22927623 | 2181-11-15 | G0378 | 2 | Hospital observation per hr |

### `hosp/labevents.csv.gz`

| labevent_id | subject_id | hadm_id | specimen_id | itemid | order_provider_id | charttime | storetime | value | valuenum | valueuom | ref_range_lower | ref_range_upper | flag | priority | comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 10000032 |  | 45421181 | 51237 | P28Z0X | 2180-03-23 11:51:00 | 2180-03-23 15:15:00 | 1.4 | 1.4 |  | 0.9 | 1.1 | abnormal | ROUTINE |  |
| 2 | 10000032 |  | 45421181 | 51274 | P28Z0X | 2180-03-23 11:51:00 | 2180-03-23 15:15:00 | ___ | 15.1 | sec | 9.4 | 12.5 | abnormal | ROUTINE | VERIFIED. |
| 3 | 10000032 |  | 52958335 | 50853 | P28Z0X | 2180-03-23 11:51:00 | 2180-03-25 11:06:00 | ___ | 15.0 | ng/mL | 30.0 | 60.0 | abnormal | ROUTINE | NEW ASSAY IN USE ___: DETECTS D2 AND D3 25-OH ACCURATELY. |
| 4 | 10000032 |  | 52958335 | 50861 | P28Z0X | 2180-03-23 11:51:00 | 2180-03-23 16:40:00 | 102 | 102.0 | IU/L | 0.0 | 40.0 | abnormal | ROUTINE |  |
| 5 | 10000032 |  | 52958335 | 50862 | P28Z0X | 2180-03-23 11:51:00 | 2180-03-23 16:40:00 | 3.3 | 3.3 | g/dL | 3.5 | 5.2 | abnormal | ROUTINE |  |

### `hosp/microbiologyevents.csv.gz`

| microevent_id | subject_id | hadm_id | micro_specimen_id | order_provider_id | chartdate | charttime | spec_itemid | spec_type_desc | test_seq | storedate | storetime | test_itemid | test_name | org_itemid | org_name | isolate_num | quantity | ab_itemid | ab_name | dilution_text | dilution_comparison | dilution_value | interpretation | comments |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 10000032 |  | 636109 | P28Z0X | 2180-03-23 00:00:00 | 2180-03-23 11:51:00 | 70093 | Blood (Toxo) | 1 | 2180-03-26 00:00:00 | 2180-03-26 10:17:00 | 90144 | TOXOPLASMA IgG ANTIBODY |  |  |  |  |  |  |  |  |  |  | NEGATIVE FOR TOXOPLASMA IgG ANTIBODY BY EIA.  0.0 IU/ML.  Reference Range:  Negative < 4 IU/ml, Positive >= 8 IU/ml.  If acute infection is suspected request IgM antibody testing and/or  submit convalescent serum in 2-3 weeks.   |
| 2 | 10000032 |  | 1836584 | P28Z0X | 2180-03-23 00:00:00 | 2180-03-23 11:51:00 | 70017 | SEROLOGY/BLOOD | 1 | 2180-03-24 00:00:00 | 2180-03-24 12:40:00 | 90127 | RUBEOLA ANTIBODY, IgG |  |  |  |  |  |  |  |  |  |  | POSITIVE BY EIA.  A positive IgG result generally indicates past exposure and/or immunity.   |
| 3 | 10000032 |  | 4131591 | P28Z0X | 2180-03-23 00:00:00 | 2180-03-23 11:51:00 | 70087 | Blood (CMV AB) | 1 | 2180-03-26 00:00:00 | 2180-03-26 10:06:00 | 90143 | CMV IgG ANTIBODY |  |  |  |  |  |  |  |  |  |  | ___ |
| 4 | 10000032 |  | 4131591 | P28Z0X | 2180-03-23 00:00:00 | 2180-03-23 11:51:00 | 70087 | Blood (CMV AB) | 2 | 2180-03-26 00:00:00 | 2180-03-26 10:06:00 | 90136 | CMV IgM ANTIBODY |  |  |  |  |  |  |  |  |  |  | NEGATIVE FOR CMV IgM ANTIBODY BY EIA.  INTERPRETATION:  INFECTION AT UNDETERMINED TIME.  A positive IgG result generally indicates past exposure.  Infection with CMV once contracted remains latent and may reactivate when immunity is compromised.  Greatly elevated serum protein with IgG levels >2000 mg/dl may cause  interference with CMV IgM results.  If current infection is suspected, submit follow-up serum in 2-3 weeks.   |
| 5 | 10000032 |  | 6028147 | P28Z0X | 2180-03-23 00:00:00 | 2180-03-23 11:51:00 | 70088 | Blood (EBV) | 1 | 2180-03-25 00:00:00 | 2180-03-25 11:54:00 | 90101 | EPSTEIN-BARR VIRUS VCA-IgG AB |  |  |  |  |  |  |  |  |  |  | POSITIVE BY EIA.   |

### `hosp/omr.csv.gz`

| subject_id | chartdate | seq_num | result_name | result_value |
| --- | --- | --- | --- | --- |
| 10000032 | 2180-04-27 | 1 | Blood Pressure | 110/65 |
| 10000032 | 2180-04-27 | 1 | Weight (Lbs) | 94 |
| 10000032 | 2180-05-07 | 1 | BMI (kg/m2) | 18.0 |
| 10000032 | 2180-05-07 | 1 | Height (Inches) | 60 |
| 10000032 | 2180-05-07 | 1 | Weight (Lbs) | 92.15 |

### `hosp/patients.csv.gz`

| subject_id | gender | anchor_age | anchor_year | anchor_year_group | dod |
| --- | --- | --- | --- | --- | --- |
| 10000032 | F | 52 | 2180 | 2014 - 2016 | 2180-09-09 |
| 10000048 | F | 23 | 2126 | 2008 - 2010 |  |
| 10000068 | F | 19 | 2160 | 2008 - 2010 |  |
| 10000084 | M | 72 | 2160 | 2017 - 2019 | 2161-02-13 |
| 10000102 | F | 27 | 2136 | 2008 - 2010 |  |

### `hosp/pharmacy.csv.gz`

| subject_id | hadm_id | pharmacy_id | poe_id | starttime | stoptime | medication | proc_type | status | entertime | verifiedtime | route | frequency | disp_sched | infusion_type | sliding_scale | lockout_interval | basal_rate | one_hr_max | doses_per_24_hrs | duration | duration_interval | expiration_value | expiration_unit | expirationdate | dispensation | fill_quantity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 11700683 | 10000032-34 | 2180-05-07 01:00:00 | 2180-05-07 22:00:00 | Acetaminophen | Unit Dose | Discontinued via patient discharge | 2180-05-07 00:09:24 | 2180-05-07 00:09:24 | PO/NG | Q6H:PRN |  |  |  |  |  |  |  |  | Ongoing | 36 | Hours |  | Omnicell |  |
| 10000032 | 22595853 | 14779570 | 10000032-22 | 2180-05-07 00:00:00 | 2180-05-07 22:00:00 | Sodium Chloride 0.9%  Flush | Unit Dose | Discontinued via patient discharge | 2180-05-07 00:00:54 | 2180-05-07 00:00:54 | IV | Q8H | 0, 8, 16 |  |  |  |  |  | 3.0 |  | Ongoing | 36 | Hours |  | Floor Stock Item |  |
| 10000032 | 22595853 | 19796602 | 10000032-50 | 2180-05-08 08:00:00 | 2180-05-07 22:00:00 | Furosemide | Unit Dose | Discontinued via patient discharge | 2180-05-07 09:32:35 | 2180-05-07 09:32:35 | PO/NG | DAILY | 08 |  |  |  |  |  | 1.0 |  | Ongoing | 36 | Hours |  | Omnicell |  |
| 10000032 | 22595853 | 20256254 | 10000032-32 | 2180-05-07 01:00:00 | 2180-05-07 22:00:00 | Raltegravir | Unit Dose | Discontinued via patient discharge | 2180-05-07 00:09:24 | 2180-05-07 00:09:24 | PO | BID | 08, 20 |  |  |  |  |  | 2.0 |  | Ongoing | 36 | Hours |  | Omnicell |  |
| 10000032 | 22595853 | 28781051 | 10000032-27 | 2180-05-07 00:00:00 | 2180-05-07 22:00:00 | Heparin | Unit Dose | Discontinued via patient discharge | 2180-05-07 00:00:54 | 2180-05-07 00:00:54 | SC | TID | 08, 14, 20 |  |  |  |  |  | 3.0 |  | Ongoing | 36 | Hours |  | Omnicell |  |

### `hosp/poe.csv.gz`

| poe_id | poe_seq | subject_id | hadm_id | ordertime | order_type | order_subtype | transaction_type | discontinue_of_poe_id | discontinued_by_poe_id | order_provider_id | order_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032-10 | 10 | 10000032 | 22595853 | 2180-05-06 20:50:49 | Lab |  | New |  |  | P9705S | Inactive |
| 10000032-100 | 100 | 10000032 | 22841357 | 2180-06-26 22:25:43 | Respiratory | Oxygen Therapy | New |  |  | P8971Q | Inactive |
| 10000032-102 | 102 | 10000032 | 22841357 | 2180-06-26 22:37:06 | Medications |  | D/C | 10000032-93 |  | P8971Q | Inactive |
| 10000032-103 | 103 | 10000032 | 22841357 | 2180-06-26 22:37:06 | Medications |  | Change | 10000032-89 |  | P8971Q | Inactive |
| 10000032-104 | 104 | 10000032 | 22841357 | 2180-06-27 07:06:36 | ADT orders | Admit | Change | 10000032-75 |  | P61HH1 | Inactive |

### `hosp/poe_detail.csv.gz`

| poe_id | poe_seq | subject_id | field_name | field_value |
| --- | --- | --- | --- | --- |
| 10000032-104 | 104 | 10000032 | Admit category | Admit to inpatient |
| 10000032-104 | 104 | 10000032 | Admit to | Medicine |
| 10000032-109 | 109 | 10000032 | Admit category | Admit to inpatient |
| 10000032-109 | 109 | 10000032 | Discharge Planning | Finalized |
| 10000032-111 | 111 | 10000032 | Admit category | Admit to inpatient |

### `hosp/prescriptions.csv.gz`

| subject_id | hadm_id | pharmacy_id | poe_id | poe_seq | order_provider_id | starttime | stoptime | drug_type | drug | formulary_drug_cd | gsn | ndc | prod_strength | form_rx | dose_val_rx | dose_unit_rx | form_val_disp | form_unit_disp | doses_per_24_hrs | route |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 11700683 | 10000032-34 | 34 | P76JEQ | 2180-05-07 01:00:00 | 2180-05-07 22:00:00 | MAIN | Acetaminophen | APAP500 | 4490.0 | 904198861 | 500mg Tablet |  | 500 | mg | 1.0 | TAB |  | PO/NG |
| 10000032 | 22595853 | 14779570 | 10000032-22 | 22 | P76JEQ | 2180-05-07 00:00:00 | 2180-05-07 22:00:00 | MAIN | Sodium Chloride 0.9%  Flush | NACLFLUSH |  | 0 | 10 mL Syringe |  | 3 | mL | 0.3 | SYR | 3.0 | IV |
| 10000032 | 22595853 | 19796602 | 10000032-50 | 50 | P260SK | 2180-05-08 08:00:00 | 2180-05-07 22:00:00 | MAIN | Furosemide | FURO40 | 8209.0 | 51079007320 | 40mg Tablet |  | 40 | mg | 1.0 | TAB | 1.0 | PO/NG |
| 10000032 | 22595853 | 20256254 | 10000032-32 | 32 | P76JEQ | 2180-05-07 01:00:00 | 2180-05-07 22:00:00 | MAIN | Raltegravir | RALT400 | 63231.0 | 6022761 | 400 mg Tablet |  | 400 | mg | 1.0 | TAB | 2.0 | PO |
| 10000032 | 22595853 | 28781051 | 10000032-27 | 27 | P76JEQ | 2180-05-07 00:00:00 | 2180-05-07 22:00:00 | MAIN | Heparin | HEPA5I | 6549.0 | 63323026201 | 5000 Units / mL- 1mL Vial |  | 5000 | UNIT | 1.0 | mL | 3.0 | SC |

### `hosp/procedures_icd.csv.gz`

| subject_id | hadm_id | seq_num | chartdate | icd_code | icd_version |
| --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 1 | 2180-05-07 | 5491 | 9 |
| 10000032 | 22841357 | 1 | 2180-06-27 | 5491 | 9 |
| 10000032 | 25742920 | 1 | 2180-08-06 | 5491 | 9 |
| 10000068 | 25022803 | 1 | 2160-03-03 | 8938 | 9 |
| 10000117 | 27988844 | 1 | 2183-09-19 | 0QS734Z | 10 |

### `hosp/provider.csv.gz`

| provider_id |
| --- |
| P0003D |
| P000DI |
| P000EW |
| P000H9 |
| P000I6 |

### `hosp/services.csv.gz`

| subject_id | hadm_id | transfertime | prev_service | curr_service |
| --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 2180-05-06 22:24:57 |  | MED |
| 10000032 | 22841357 | 2180-06-26 18:28:08 |  | MED |
| 10000032 | 25742920 | 2180-08-05 23:44:50 |  | MED |
| 10000032 | 29079034 | 2180-07-23 12:36:04 |  | MED |
| 10000068 | 25022803 | 2160-03-03 23:17:17 |  | MED |

### `hosp/transfers.csv.gz`

| subject_id | hadm_id | transfer_id | eventtype | careunit | intime | outtime |
| --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 22595853 | 33258284 | ED | Emergency Department | 2180-05-06 19:17:00 | 2180-05-06 23:30:00 |
| 10000032 | 22595853 | 35223874 | admit | Transplant | 2180-05-06 23:30:00 | 2180-05-07 17:21:27 |
| 10000032 | 22595853 | 36904543 | discharge |  | 2180-05-07 17:21:27 |  |
| 10000032 | 22841357 | 34100253 | discharge |  | 2180-06-27 18:49:12 |  |
| 10000032 | 22841357 | 34703856 | admit | Transplant | 2180-06-26 21:31:00 | 2180-06-27 18:49:12 |

## `icu/` 目录

### `icu/caregiver.csv.gz`

| caregiver_id |
| --- |
| 10 |
| 17 |
| 20 |
| 25 |
| 27 |

### `icu/chartevents.csv.gz`

| subject_id | hadm_id | stay_id | caregiver_id | charttime | storetime | itemid | value | valuenum | valueuom | warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | 47007 | 2180-07-23 21:01:00 | 2180-07-23 22:15:00 | 220179 | 82 | 82 | mmHg | 0 |
| 10000032 | 29079034 | 39553978 | 47007 | 2180-07-23 21:01:00 | 2180-07-23 22:15:00 | 220180 | 59 | 59 | mmHg | 0 |
| 10000032 | 29079034 | 39553978 | 47007 | 2180-07-23 21:01:00 | 2180-07-23 22:15:00 | 220181 | 63 | 63 | mmHg | 0 |
| 10000032 | 29079034 | 39553978 | 47007 | 2180-07-23 22:00:00 | 2180-07-23 22:15:00 | 220045 | 94 | 94 | bpm | 0 |
| 10000032 | 29079034 | 39553978 | 47007 | 2180-07-23 22:00:00 | 2180-07-23 22:15:00 | 220179 | 85 | 85 | mmHg | 0 |

### `icu/d_items.csv.gz`

| itemid | label | abbreviation | linksto | category | unitname | param_type | lownormalvalue | highnormalvalue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 220001 | Problem List | Problem List | chartevents | General |  | Text |  |  |
| 220003 | ICU Admission date | ICU Admission date | datetimeevents | ADT |  | Date and time |  |  |
| 220045 | Heart Rate | HR | chartevents | Routine Vital Signs | bpm | Numeric |  |  |
| 220046 | Heart rate Alarm - High | HR Alarm - High | chartevents | Alarms | bpm | Numeric |  |  |
| 220047 | Heart Rate Alarm - Low | HR Alarm - Low | chartevents | Alarms | bpm | Numeric |  |  |

### `icu/datetimeevents.csv.gz`

| subject_id | hadm_id | stay_id | caregiver_id | charttime | storetime | itemid | value | valueuom | warning |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | 66056 | 2180-07-23 21:02:00 | 2180-07-23 21:02:00 | 225754 | 2180-07-23 00:00:00 | Date | 0 |
| 10000032 | 29079034 | 39553978 | 66056 | 2180-07-23 21:02:00 | 2180-07-23 21:02:00 | 225755 | 2180-07-23 00:00:00 | Date | 0 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 14:24:00 | 2180-07-23 14:24:00 | 225754 | 2180-07-23 14:24:00 | Date | 0 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 14:24:00 | 2180-07-23 14:24:00 | 225755 | 2180-07-23 14:24:00 | Date | 0 |
| 10000980 | 26913865 | 39765666 | 36518 | 2189-06-27 09:13:00 | 2189-06-27 09:13:00 | 225755 | 2189-06-27 09:13:00 | Date | 0 |

### `icu/icustays.csv.gz`

| subject_id | hadm_id | stay_id | first_careunit | last_careunit | intime | outtime | los |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2180-07-23 14:00:00 | 2180-07-23 23:50:47 | 0.4102662037037037 |
| 10000980 | 26913865 | 39765666 | Medical Intensive Care Unit (MICU) | Medical Intensive Care Unit (MICU) | 2189-06-27 08:42:00 | 2189-06-27 20:38:27 | 0.4975347222222222 |
| 10001217 | 24597018 | 37067082 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2157-11-20 19:18:02 | 2157-11-21 22:08:00 | 1.1180324074074075 |
| 10001217 | 27703517 | 34592300 | Surgical Intensive Care Unit (SICU) | Surgical Intensive Care Unit (SICU) | 2157-12-19 15:42:24 | 2157-12-20 14:27:41 | 0.9481134259259258 |
| 10001725 | 25563031 | 31205490 | Medical/Surgical Intensive Care Unit (MICU/SICU) | Medical/Surgical Intensive Care Unit (MICU/SICU) | 2110-04-11 15:52:22 | 2110-04-12 23:59:56 | 1.338587962962963 |

### `icu/ingredientevents.csv.gz`

| subject_id | hadm_id | stay_id | caregiver_id | starttime | endtime | storetime | itemid | amount | amountuom | rate | rateuom | orderid | linkorderid | statusdescription | originalamount | originalrate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | 66056 | 2180-07-23 21:10:00 | 2180-07-23 21:11:00 | 2180-07-23 21:10:00 | 220490 | 100.0 | ml |  |  | 415918 | 415918 | FinishedRunning | 0 | 100 |
| 10000032 | 29079034 | 39553978 | 66056 | 2180-07-23 21:10:00 | 2180-07-23 21:11:00 | 2180-07-23 21:10:00 | 227075 | 100.0 | ml |  |  | 415918 | 415918 | FinishedRunning | 0 | 100 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 17:00:00 | 2180-07-23 17:01:00 | 2180-07-23 18:56:00 | 220490 | 200.0 | ml |  |  | 7140773 | 7140773 | FinishedRunning | 0 | 200 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 17:00:00 | 2180-07-23 17:01:00 | 2180-07-23 18:56:00 | 227075 | 200.0 | ml |  |  | 7140773 | 7140773 | FinishedRunning | 0 | 200 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 17:00:00 | 2180-07-23 17:30:00 | 2180-07-23 17:02:00 | 220490 | 49.999998807907104 | ml | 100.0 | mL/hour | 7578214 | 7578214 | FinishedRunning | 0 | 50 |

### `icu/inputevents.csv.gz`

| subject_id | hadm_id | stay_id | caregiver_id | starttime | endtime | storetime | itemid | amount | amountuom | rate | rateuom | orderid | linkorderid | ordercategoryname | secondaryordercategoryname | ordercomponenttypedescription | ordercategorydescription | patientweight | totalamount | totalamountuom | isopenbag | continueinnextdept | statusdescription | originalamount | originalrate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | 66056 | 2180-07-23 21:10:00 | 2180-07-23 21:11:00 | 2180-07-23 21:10:00 | 226452 | 100.0 | ml |  |  | 415918 | 415918 | 14-Oral/Gastric Intake |  | Main order parameter | Bolus | 39.4 | 100 | ml | 0 | 0 | FinishedRunning | 100 | 100 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 17:00:00 | 2180-07-23 17:01:00 | 2180-07-23 18:56:00 | 226452 | 200.0 | ml |  |  | 7140773 | 7140773 | 14-Oral/Gastric Intake |  | Main order parameter | Bolus | 39.4 | 200 | ml | 0 | 0 | FinishedRunning | 200 | 200 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 17:00:00 | 2180-07-23 17:30:00 | 2180-07-23 17:02:00 | 220862 | 49.999998807907104 | ml | 100.0 | mL/hour | 7578214 | 7578214 | 04-Fluids (Colloids) |  | Main order parameter | Continuous IV | 39.4 | 50 | ml | 0 | 0 | FinishedRunning | 50 | 100 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 17:33:00 | 2180-07-23 18:03:00 | 2180-07-23 18:16:00 | 220862 | 49.999998807907104 | ml | 100.0 | mL/hour | 427849 | 427849 | 04-Fluids (Colloids) |  | Main order parameter | Continuous IV | 39.4 | 50 | ml | 0 | 0 | FinishedRunning | 50 | 100 |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 18:56:00 | 2180-07-23 18:57:00 | 2180-07-23 18:56:00 | 226452 | 100.0 | ml |  |  | 1579487 | 1579487 | 14-Oral/Gastric Intake |  | Main order parameter | Bolus | 39.4 | 100 | ml | 0 | 0 | FinishedRunning | 100 | 100 |

### `icu/outputevents.csv.gz`

| subject_id | hadm_id | stay_id | caregiver_id | charttime | storetime | itemid | value | valueuom |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | 88981 | 2180-07-23 15:00:00 | 2180-07-23 16:00:00 | 226560 | 175 | ml |
| 10000980 | 26913865 | 39765666 | 36518 | 2189-06-27 09:08:00 | 2189-06-27 09:08:00 | 226559 | 450 | ml |
| 10000980 | 26913865 | 39765666 | 36518 | 2189-06-27 09:08:00 | 2189-06-27 09:08:00 | 226633 | 400 | ml |
| 10000980 | 26913865 | 39765666 | 36518 | 2189-06-27 11:00:00 | 2189-06-27 10:51:00 | 226559 | 600 | ml |
| 10000980 | 26913865 | 39765666 | 36518 | 2189-06-27 13:00:00 | 2189-06-27 12:55:00 | 226559 | 800 | ml |

### `icu/procedureevents.csv.gz`

| subject_id | hadm_id | stay_id | caregiver_id | starttime | endtime | storetime | itemid | value | valueuom | location | locationcategory | orderid | linkorderid | ordercategoryname | ordercategorydescription | patientweight | isopenbag | continueinnextdept | statusdescription | originalamount | originalrate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10000032 | 29079034 | 39553978 | 88981.0 | 2180-07-23 14:43:00 | 2180-07-23 14:44:00 | 2180-07-23 14:43:00 | 225966 | 1 |  |  |  | 6416557 | 6416557 | Procedures | Task | 39.4 | 0 | 0 | FinishedRunning | 1 | 0 |
| 10000032 | 29079034 | 39553978 |  | 2180-07-23 14:24:00 | 2180-07-23 23:50:00 | 2180-07-23 23:50:49.983 | 224275 | 566 | min |  |  | 6497934 | 6497934 | Peripheral Lines | ContinuousProcess | 39.4 | 1 | 0 | FinishedRunning | 566 | 1 |
| 10000032 | 29079034 | 39553978 |  | 2180-07-23 14:24:00 | 2180-07-23 23:50:00 | 2180-07-23 23:50:49.983 | 224277 | 566 | min |  |  | 9643097 | 9643097 | Peripheral Lines | ContinuousProcess | 39.4 | 1 | 0 | FinishedRunning | 566 | 1 |
| 10000980 | 26913865 | 39765666 |  | 2189-06-27 09:01:00 | 2189-06-27 20:38:00 | 2189-06-27 20:38:29.047 | 225794 | 697 | min |  |  | 5989583 | 5989583 | Ventilation | ContinuousProcess | 76.2 | 1 | 0 | FinishedRunning | 697 | 1 |
| 10000980 | 26913865 | 39765666 |  | 2189-06-27 09:15:00 | 2189-06-27 20:38:00 | 2189-06-27 20:38:29.047 | 224277 | 683 | min |  |  | 476764 | 476764 | Peripheral Lines | ContinuousProcess | 76.2 | 1 | 0 | FinishedRunning | 683 | 1 |

