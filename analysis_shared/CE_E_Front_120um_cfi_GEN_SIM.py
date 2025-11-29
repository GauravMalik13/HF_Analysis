# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: CE_E_Front_120um_cfi -s GEN,SIM -n 10 --conditions auto:phase2_realistic_T33 --beamspot HGCALCloseBy --datatier GEN-SIM --eventcontent FEVTDEBUG --geometry ExtendedRun4D110 --era Phase2C17I13M9 --relval 9000,100 --no_exec --fileout file:step1.root

# This code has been modified to shoot electrons and positrons to HF.

import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('SIM', Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')

# The below geometry is for HGCal
# process.load('Configuration.Geometry.GeometryExtendedRun4D110Reco_cff')
# process.load('Configuration.Geometry.GeometryExtendedRun4D110_cff')

# Tried the below geometries but did not work
#process.load('Configuration.Geometry.GeometryExtended2021Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2021_cff')

# This worked for HF
process.load('Configuration.StandardSequences.GeometrySimDB_cff')

process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
# process.load('IOMC.EventVertexGenerators.VtxSmearedHGCALCloseBy_cfi')

# Using a standard realistic beamspot for Run 3 as an example
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13p6TeVEarly2022Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# No of Events
process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(10000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('CE_E_Front_120um_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

process.generator = cms.EDProducer("CloseByParticleGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        ControlledByEta = cms.bool(True),
        Delta = cms.double(10),
        FlatPtGeneration = cms.bool(False),
                                        
        VarMin = cms.double(25.0),      # In GeV (default values 25 - 200 GeV)
        VarMax = cms.double(200.0),
        MaxVarSpread = cms.bool(False),  # if True, Var = P_t; if False, Var = Energy 
        
        MinEta = cms.double(3.1),           # Eta of HF is in range of (3.0 - 5.2), To not have edge effects we use a reduced
        MaxEta = cms.double(5.0),
                                            # range of (3.1 - 5.0)
        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359),
        
        ZMin = cms.double(1119.9),           # Position of Primary vertex formation range in HF
        ZMax = cms.double(1120.1),          # Position of HF along Z axis from origin (in cm)

        RMin = cms.double(15.0),            # Corresponding R for Z=11.2m, eta=5.0
        RMax = cms.double(105.0),           # Corresponding R for Z=11.2m, eta=3.1

        NParticles = cms.int32(1),          # No of Particles
        OffsetFirst = cms.double(0.0),
        Overlapping = cms.bool(False),
        
        PartID = cms.vint32(11, -11),       # 11 for electrons, -11 for positrons
        Pointing = cms.bool(True),          # if True the particles will point to the origin, else will be parallel to the beam
                                            # axis
        
        RandomShoot = cms.bool(False),      # Shoots random # particles between 1 to NParticles.
        
        TMax = cms.double(0.05),            # Time range of production of particle (in ns)
        TMin = cms.double(0.0),             # relative to the event time t = 0
        UseDeltaT = cms.bool(False),
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('random particles in phi and r windows')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

