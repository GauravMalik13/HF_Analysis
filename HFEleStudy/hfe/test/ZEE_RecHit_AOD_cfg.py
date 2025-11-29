import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
# process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )


process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1)

options = VarParsing.VarParsing('standard')

options.register('inputFile',
        "~/",
        VarParsing.VarParsing.multiplicity.singleton,
        VarParsing.VarParsing.varType.string,
        "File containing a list of the EXACT location of the output file  (default = ~/)"
        )


options.parseArguments()
options.inputFile = 'root://eoscms//' + options.inputFile
print(options.inputFile)
process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(
           'file:step3.root'),

                )


process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_mc_GRun', '')



process.nTuplelize = cms.EDAnalyzer('ZEE_RecHit_NTuplizer',
        electrons = cms.InputTag("gedGsfElectrons")
        # slimmedElectrons = cms.InputTag("slimmedElectrons")
	)


process.TFileService = cms.Service("TFileService",

     fileName = cms.string("nTuple_MC.root"),
      closeFileFast = cms.untracked.bool(True)
  )


process.p = cms.Path(process.nTuplelize)

