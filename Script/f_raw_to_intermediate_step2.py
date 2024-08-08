"""
This is a document about how we construct Intermediate Step 2
"""

def typo_cleaning(x):
    if x=='Agent Orange &Dioxin':
        x='Agent Orange & Dioxin'
    elif x=='Agent Orange &amp':
        x='Agent Orange & Dioxin'
    elif x=='American Indian or Alaska Native':
        x='American Indians / Alaska Natives'        
    elif x=='Cannabidiol Research':
        x='Cannabinoid Research'        
    elif x=='Chronic Fatigue Syndrome':
        x='Chronic Fatigue Syndrome (ME/CFS)' 
    elif x=='Conditions affecting unborn children':
        x='Conditions Affecting the Embryonic and Fetal Periods' 
    elif x=='D':
        x=''  
    elif x=='Infant Mortality/ (LBW)':
        x='Infant Mortality'  
    elif x=='Networking and Information Technology R&amp':
        x='Networking and Information Technology R&D'  
    elif x=='Pneumonia &Influenza':
        x='Pneumonia & Influenza'   
    elif x=='Pneumonia &amp':
        x='Pneumonia & Influenza'
    else:
        x = x
    return x
        

def uniform_cats(x): # (they are all mutually exclusive adjustments!)
    # (1) corrections after realizing that category appears with n projects >0 for just 1/2 years and is not merged to anything else  
    if x=='Behavioral Changes Interventions that Delay onset of Sexual Activity':
        x=''         
    elif x=='Biodefense - Biodefense Research':
        x='' 
    elif x=='Biodefense - Biodefense Research - Antibiotics/Antiviral':
        x=''        
    elif x=='Biodefense - Biodefense Research - Basic Research (Genomics and Pathogenesis)':
        x=''        
    elif x=='Biodefense - Biodefense Research - Diagnostics':
        x=''        
    elif x=='Biodefense - Biodefense Research - Vaccines':
        x=''        
    elif x=='Biodefense - Chemical Countermeasures':
        x='' 
    elif x=='Biodefense - Nuclear/Radiological Countermeasures':
        x='' 
    elif x=='Chemical Preparedness and Decontamination Activities':
        x='' 
    elif x=='Childhood Obesity':
        x=''             
    elif x=='Clinical Center Assessments':
        x='' 
    elif x=='Clinical Research - Extramural':
        x='' 
    elif x=='Complementary and Integrative Health':
        x='' 
    elif x=='Creutzfeldt-Jakob':
        x='' 
    elif x=='DIS Limb Regeneration':
        x='' 
    elif x=='Data Science':
        x='' 
    elif x=='Dioxin':
        x='' 
    elif x=='Firearms Research':
        x=''        
    elif x=='Food Defense':
        x=''         
    elif x=='Health Disparities Related':
        x=''        
    elif x=='Hearing Loss':
        x=''    
    elif x=='Immunotherapy':
        x=''          
    elif x=='Kidney and Urologic - End Stage Renal Disease':
        x='' 
    elif x=='Kidney and Urologic - Incontinence':
        x='' 
    elif x=='Kidney and Urologic - Prostate Disease':
        x='' 
    elif x=='Kidney and Urologic - Urinary Infection':
        x='' 
    elif x=='Kidney and Urologic Diseases inc. Nephritis':
        x=''   
    elif x=='Machine Learning and Artificial Intelligence':
        x=''     
    elif x=='Microbiome':
        x=''            
    elif x=='Nanotechnology - Fundamental nanoscale phenomena and processes':
        x=''  
    elif x=='Nanotechnology - Instrumentation research, metrology, and standards for nanotechnology':
        x=''  
    elif x=='Nanotechnology - Major research facilities and instrumentation acquisition':
        x=''  
    elif x=='Nanotechnology - Nanomanufacturing':
        x=''  
    elif x=='Nanotechnology - Nanomaterial':
        x=''  
    elif x=='Nanotechnology - Nanoscale devices and systems':
        x=''  
    elif x=='Nanotechnology - Societal Dimensions':
        x=''  
    elif x=='Nanotechnology - Societal Dimensions - Environmental, Health and Safety Implications':
        x=''  
    elif x=='Nanotechnology - Societal Dimensions - Societal Dimensions other than EHS':
        x=''                  
    elif x=='Networking and Information Technology R&D - Cyber security and information assurance':
        x=''  
    elif x=='Networking and Information Technology R&D - High confidence software and systems':
        x=''  
    elif x=='Networking and Information Technology R&D - High-end computing R&D':
        x=''  
    elif x=='Networking and Information Technology R&D - High-end computing infrastructure and applications':
        x=''  
    elif x=='Networking and Information Technology R&D - High-end infrastructure and applications':
        x=''  
    elif x=='Networking and Information Technology R&D - Human computer interaction and information management':
        x=''  
    elif x=='Networking and Information Technology R&D - Large scale networking':
        x=''                  
    elif x=='Networking and Information Technology R&D - Social, economic, and workforce implications of IT and IT workforce development':
        x=''         
    elif x=='Networking and Information Technology R&D - Software design and productivity':
        x='' 
    elif x=='Opioid Misuse and Addiction':
        x=''         
    elif x=='Opioids':
        x=''            
    elif x=="Stem Cell Research - Umbilical Cord Blood/ Placenta - Human - Basic &Other Clinical Research":
        x='' 
    elif x=="Stem Cell Research - Umbilical Cord Blood/ Placenta - Human - Clinical Trials":
        x='' 
    elif x=="Stem Cell Research - Umbilical Cord Blood/ Placenta - Non-Human - Basic &Other Clinical Research":
        x='' 
    elif x=="Translational Research":
        x=''    



    # (2) corrections after realizing that category changed name over time, so need to merge/collapse categories into 1
    elif x=='Alcoholism, Alcohol Use and Health':
        x='Alcoholism'  
    elif x=='Pain Conditions - Chronic':
        x='Chronic Pain' 
    elif x=='Climate-Related Exposures and Conditions':
        x='Health Effects of Climate Change' 
    elif x=='Clinical Trials':
        x='Clinical Trials and Supportive Activities' 
    elif x=='Mental Retardation (Intellectual and Developmental Disabilities (IDD))':
        x='Intellectual and Developmental Disabilities (IDD)'             
    elif x=='Networking and Information Technology R&D':
        x='Networking and Information Technology R&D (NITRD)'          
    elif x=="Sepsis":
        x='Septicemia' 
    elif x=="Substance Abuse Prevention":
        x='Substance Abuse' 
    elif x=="Tobacco Smoke and Health":
        x='Smoking and Health'            
    elif x=="Youth Violence":
        x='Youth Violence Prevention'   
    elif x=="Preterm, Low Birth Weight and Health of the Newborn":
        x="Perinatal - Birth - Preterm (LBW)"                     
    elif x=="Neonatal Respiratory Distress":
        x="Perinatal - Neonatal Respiratory Distress Syndrome"  

   
    
    
    # (3) correction if clear that they are (already included) subsets of larger cat (and we don't care about subdivision in subsets)
    # --> when collapsing funding, if same proj is associated to main and subcat, duplicates will be dropped so will not be counted twice
    elif x=="Stem Cell Research - Embryonic - Human":
        x='Stem Cell Research'        
    elif x=="Stem Cell Research - Embryonic - Non-Human":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Induced Pluripotent Stem Cell":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Induced Pluripotent Stem Cell - Human":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Induced Pluripotent Stem Cell - Non-Human":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Nonembryonic - Human":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Nonembryonic - Non-Human":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Umbilical Cord Blood/ Placenta":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Umbilical Cord Blood/ Placenta - Human":
        x='Stem Cell Research'  
    elif x=="Stem Cell Research - Umbilical Cord Blood/ Placenta - Non-Human":
        x='Stem Cell Research'  
    
    elif x=="Injury - Childhood Injuries":
        x='Injury (total) Accidents/Adverse Effects' 
    elif x=="Injury - Trauma - (Head and Spine)":
        x='Injury (total) Accidents/Adverse Effects'              
    elif x=="Injury - Traumatic brain injury":
        x='Injury (total) Accidents/Adverse Effects' 
    elif x=="Injury - Unintentional Childhood Injury":
        x='Injury (total) Accidents/Adverse Effects'         
    elif x=="Spinal Cord Injury": # add to the borader group of injury, likely not included in counting differently from subgroups above
        x="Injury (total) Accidents/Adverse Effects"        


    # elif x=="Digestive Diseases - (Gallbladder)":
    #     x="Digestive Diseases" 
    # elif x=="Digestive Diseases - (Peptic Ulcer)":
    #     x="Digestive Diseases"
        
    # elif x=="Heart Disease - Coronary Heart Disease":
    #     x="Heart Disease"  

    elif x=="Pneumonia": # already counted in penumonia & influenczs cat
        x="Pneumonia & Influenza" 
    elif x=="Influenza":
        x="Pneumonia & Influenza" 
    
    # elif x=="Hepatitis - A":
    #     x="Hepatitis"         
    # elif x=="Hepatitis - B":
    #     x="Hepatitis" 
    # elif x=="Hepatitis - C":
    #     x="Hepatitis"         

    # 3bis: since we don't have burden data about specific subcategories, but we do have them for the larger cat, aggregate at the larger category
    # elif x=="Infant Mortality": # group all togetehr because they all belong to prenatal/natal + don't have burden data about specific types of prenatal cause
    #     x="Perinatal and neonatal conditions"   
    # elif x=="Sudden Infant Death Syndrome":
    #     x="Perinatal and neonatal conditions"  
    # elif x=="Preterm, Low Birth Weight and Health of the Newborn":
    #    x="Perinatal and neonatal conditions"              
    # elif x=="Perinatal - Birth - Preterm (LBW)":
    #    x="Perinatal and neonatal conditions"        
    # elif x=="Neonatal Respiratory Distress":
    #    x="Perinatal and neonatal conditions"  
    # elif x=="Perinatal - Neonatal Respiratory Distress Syndrome":
    #    x="Perinatal and neonatal conditions"          
    # elif x=="Perinatal Period - Conditions Originating in Perinatal Period":
    #    x="Perinatal and neonatal conditions"  
       
    # elif x=="Macular Degeneration":
    #    x="Eye Disease and Disorders of Vision"       
       
    # elif x=="Temporomandibular Muscle/Joint Disorder (TMJD)":
    #    x="Dental/Oral and Craniofacial Disease"          

    # elif x=="Post-Traumatic Stress Disorder (PTSD)":
    #    x="Anxiety Disorders"  
       
    # 3tris: subset starts from a certain date, as if from T NIH wanted to be even more precise about the subcategory.
    # --> so keeping the subcategory and not the main would have meant reducing the analysisi to very few time periods
    elif x=="Serious Mental Illness": # this subset starts from a certain date, as if from T NIH wanted to be even more precise about the subcategory
        x="Mental Illness" 
    elif x=="Major Depressive Disorder": # this subset starts from a certain date, as if from T NIH wanted to be even more precise about the subcategory
        x="Depression" 
    # elif x=="Osteoarthritis": # this subset starts from a certain date, as if from T NIH wanted to be even more precise about the subcategory
    #     x="Arthritis"         
    # elif x=="Rheumatoid Arthritis": # this subset starts from a certain date, as if from T NIH wanted to be even more precise about the subcategory
    #     x="Arthritis" 


    # (4) correction after checking footnote in this website: https://report.nih.gov/funding/categorical-spending#/    
    elif x=="Alzheimer's Disease Related Dementias (ADRD)": # supercategory including minor ones below, which also changed over t. So we prefer to aggregate minor cat into one that we define
        x="Alzheimer's Disease and Related Dementias"
    elif x=="Alzheimer's Disease including Alzheimer's Disease Related Dementias (AD/ADRD)": # supercategory including minor ones below, which also changed over t. So we prefer to aggregate minor cat into one that we define
        x="Alzheimer's Disease and Related Dementias"
    elif x=="Frontotemporal Dementia (FTD)":
        x="Alzheimer's Disease and Related Dementias"
    elif x=="Lewy Body Dementia":
        x="Alzheimer's Disease and Related Dementias"
    elif x=="Vascular Cognitive Impairment/Dementia":
        x="Alzheimer's Disease and Related Dementias"
    elif x=="Alzheimer's Disease":
        x="Alzheimer's Disease and Related Dementias"
        
    elif x=="Biodefense": # categorization follows rules from another entity
        x=""   
    elif x=="Biomedical Imaging":
        x="Diagnostic Radiology"   
    elif x=="Childhood Injury":
        x="Injury - Childhood Injuries"        
    elif x=="Drug Abuse (NIDA only)": # categorization follows rules from another entity
        x="" 
    elif x=="Food Safety": 
        x="Foodborne Illness"     
    elif x=="Peripheral Neuropathy":
         x="Neuropathy"    
    elif x=="Sexually Transmitted Diseases/Herpes":
        x="Sexually Transmitted Infections"           
    elif x=="Headaches":
        x="Migraines"  
    elif x=="Anorexia": # note explicitely mentions that it is included in eating disorders
        x="Eating Disorders"          
               
    

    else:
        x = x
        
    return x
    
   