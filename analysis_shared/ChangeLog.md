# HF Analysis

## Tables of Content

- [Step 1](#changelog-for-step-1)
- [Step 2](#changelog-for-step-2)
- [Step 3](#changelog-for-step-3)

## Information

Original code (Unmodified) could be found in the `original` folder in the directory.

`(...)`: Used to describe or add information.

`[...]`: Used to indicate Line Number.

Beyond Step 2, The above convention is used.

## ChangeLog for Step 1 

fileName : `CE_E_Front_120um_cfi_GEN_SIM.py` 

### Changes :
* Era (used Run3) [line 11]

* Geometry (used GeometryDB) [line 31 ]

* Event Vertex Generator [line 38]

* GlobalTag (Changed to phase1_2022_realistic) [line 112]

* Parameters of the particle gun [line 114]:
    * PartId = [11,-11]    // for $e^-/e^+$
    
    * VarMin = 25 GeV
    
    * VarMax = 200 GeV
    
    * FlatPtGeneration = False // If false Var =  Energy; if true Var = $P_t$
    
    * MinEta = 3.1  // Originally $3.0 \leq | \eta | \leq 5.2 $
    
    * MaxEta = 5.0
    
    * MinPhi = $-\pi$
    
    * MaxPhi = $\pi$
    
    * ZMin = 1119.9 cm //This is responsible for the range of position of primary vertex formation in HF.
    
    * ZMax = 1120.1 cm
    
    * RMin = 15.0 cm   // Inner Radius of HF = 12.5 cm
    
    * RMax = 105 cm	// Outer Radius of HF = 130 cm
    
    * NParticles = 1	// No of Particles

Rest everything is same as in the file.

<b>Output: </b> `step1.root`

## ChangeLog for Step 2 

fileName: `step2_DIGI_L1TrackTrigger_L1_L1P2GT_DIGI2RAW_HLT.py` 

### Changes : 
* Era (Same as Step 1)

* ticl (Removed ticl) [Line 13-14]

* Geometry ( Used GeometrySimDB & GeometryRecoDB) [Line 25-26]

* L1TrackTrigger (Removed) [Line 28 - 33]

* Removed SimPhase2L1GlobalTriggerEmulator and l1tGTMenu [Line 36-37]

* HLTrigger (Changed HLTrigger from HLT_75e33 to HLT_Fake2) [Line 40 - 42]

* GlobalTag (same as step 1 : phase1_2022_realistic) [Line 143]

* Path (Commented a lot of lines) [Line 146, 150 - 193, 198]
* Schedule (Commented a lot of lines) [Line 202, 206 - 249, 

Rest all same.

<b>Output : </b>`step2.root`

## ChangeLog for Step 3

fileName : `step3_RAW2DIGI_RECO_RECOSIM_PAT_VALIDATION_DQM.py`

### Changes : 

* Eras (Same as Step 1, 2) [8]

* ticl (Removed) [9 - 11]

* Geometry (Used `GeometryRecoDB`) [23]

* GlobalTag (same as step 1, 2 : `phase1_2022_realistic`) [189]

* Path (Commented some steps) [225, 226, 233, 239 - 243, 249, 253, 254, 260-262, 269]

* Schedule (Commented Path Steps have been removed, Appropriate space has been left to indicate the removed step) [280]

* Commented lines 315, 316

<b>Output :</b> (in Descending Order of file size)

1. `step3.root`
2. `step3_inMINIAODSIM.root`
3. `step3_inDQM.root`



