import FWCore.ParameterSet.Config as cms


from Analysis.VLQAna.JetSelector_cfi import *

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_1.root',
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_2.root',
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_3.root',
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_4.root',
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_5.root',
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_6.root',
	'file:/home/t3-ku/erichjs/store/b2g/PHYS14/QCD_HT-500To1000_13TeV-madgraph/v1_edmntuple_B2GAnaFW/150223_172532/0000/B2GEDMNtuple_7.root',
    )
)

process.analyze = cms.EDAnalyzer('TprimeAna'
)


process.presel = cms.EDFilter("VLQAna",
    processName                = cms.string  ('@'), 
    trigNameLabel              = cms.InputTag("TriggerUserData", "triggerNameTree"), 
    trigBitLabel               = cms.InputTag("TriggerUserData", "triggerBitTree"), 
    jetAK8PtLabel              = cms.InputTag("jetsAK8", "jetAK8Pt"),
    jetAK8EtaLabel             = cms.InputTag("jetsAK8", "jetAK8Eta"),
    jetAK8PhiLabel             = cms.InputTag("jetsAK8", "jetAK8Phi"),
    jetAK8MassLabel            = cms.InputTag("jetsAK8", "jetAK8Mass"),
    jetAK8FilteredMassLabel    = cms.InputTag("jetsAK8", "jetAK8filteredMass"),
    jetAK8PrunedMassLabel      = cms.InputTag("jetsAK8", "jetAK8prunedMass"),
    jetAK8TrimmedMassLabel     = cms.InputTag("jetsAK8", "jetAK8trimmedMass"),
    jetAK8EnergyLabel          = cms.InputTag("jetsAK8", "jetAK8Energy"),
    jetAK8FlavourLabel         = cms.InputTag("jetsAK8", "jetAK8Flavour"),
    jetAK8CSVLabel             = cms.InputTag("jetsAK8", "jetAK8CSV"),
    jetAK8JECLabel             = cms.InputTag("jetsAK8", "jetAK8jecFactor0"),
    jetAK8AreaLabel            = cms.InputTag("jetsAK8", "jetAK8jetArea"),
    jetAK8Tau1Label            = cms.InputTag("jetsAK8", "jetAK8tau1"), 
    jetAK8Tau2Label            = cms.InputTag("jetsAK8", "jetAK8tau2"),  
    jetAK8Tau3Label            = cms.InputTag("jetsAK8", "jetAK8tau3"),  
    jetAK8nSubJetsLabel        = cms.InputTag("jetsAK8", "jetAK8nSubJets"),  
    jetAK8minmassLabel         = cms.InputTag("jetsAK8", "jetAK8minmass"),  
    jetAK8VSubjetIndex0Label   = cms.InputTag("jetsAK8", "jetAK8VSubjetIndex0"),  
    jetAK8VSubjetIndex1Label   = cms.InputTag("jetsAK8", "jetAK8VSubjetIndex1"),  
    jetAK8TopSubjetIndex0Label = cms.InputTag("jetsAK8", "jetAK8TopSubjetIndex0"),
    jetAK8TopSubjetIndex1Label = cms.InputTag("jetsAK8", "jetAK8TopSubjetIndex1"),
    jetAK8TopSubjetIndex2Label = cms.InputTag("jetsAK8", "jetAK8TopSubjetIndex2"),
    jetAK8TopSubjetIndex3Label = cms.InputTag("jetsAK8", "jetAK8TopSubjetIndex3"),
    subjetAK8BDiscLabel        = cms.InputTag("subjetsAK8", "subjetAK8subjetCSV"),
    subjetAK8PtLabel           = cms.InputTag("subjetsAK8", "subjetAK8Pt"),
    subjetAK8EtaLabel          = cms.InputTag("subjetsAK8", "subjetAK8Eta"),
    subjetAK8PhiLabel          = cms.InputTag("subjetsAK8", "subjetAK8Phi"),
    subjetAK8MassLabel         = cms.InputTag("subjetsAK8", "subjetAK8Mass"),
    subjetCmsTopTagBDiscLabel  = cms.InputTag("subjetsCmsTopTag", "subjetsCmsTopTagCSV"),
    subjetCmsTopTagPtLabel     = cms.InputTag("subjetsCmsTopTag", "subjetsCmsTopTagPt"),
    subjetCmsTopTagEtaLabel    = cms.InputTag("subjetsCmsTopTag", "subjetsCmsTopTagEta"),
    subjetCmsTopTagPhiLabel    = cms.InputTag("subjetsCmsTopTag", "subjetsCmsTopTagPhi"),
    subjetCmsTopTagMassLabel   = cms.InputTag("subjetsCmsTopTag", "subjetsCmsTopTagMass"),
    jetAK4PtLabel              = cms.InputTag("jetsAK4", "jetAK4Pt"),
    jetAK4EtaLabel             = cms.InputTag("jetsAK4", "jetAK4Eta"),
    jetAK4PhiLabel             = cms.InputTag("jetsAK4", "jetAK4Phi"),
    jetAK4MassLabel            = cms.InputTag("jetsAK4", "jetAK4Mass"),
    jetAK4EnergyLabel          = cms.InputTag("jetsAK4", "jetAK4Energy"),
    jetAK4FlavourLabel         = cms.InputTag("jetsAK4", "jetAK4Flavour"),
    jetAK4CSVLabel             = cms.InputTag("jetsAK4", "jetAK4CSV"),
    jetAK4JECLabel             = cms.InputTag("jetsAK4", "jetAK4jecFactor0"),
    jetAK4nHadEnergyLabel      = cms.InputTag("jetsAK4", "jetAK4neutralHadronEnergy"),
    jetAK4nEMEnergyLabel       = cms.InputTag("jetsAK4", "jetAK4neutralEmEnergy"),
    jetAK4HFHadronEnergyLabel  = cms.InputTag("jetsAK4", "jetAK4HFHadronEnergy"),
    jetAK4cHadEnergyLabel      = cms.InputTag("jetsAK4", "jetAK4chargedHadronEnergy"),
    jetAK4cEMEnergyLabel       = cms.InputTag("jetsAK4", "jetAK4chargedEmEnergy"),
    jetAK4numDaughtersLabel    = cms.InputTag("jetsAK4", "jetAK4numberOfDaughters"),
    jetAK4cMultipLabel         = cms.InputTag("jetsAK4", "jetAK4chargedMultiplicity"),
    jetAK4YLabel               = cms.InputTag("jetsAK4", "jetAK4Y"),
    jetAK4AreaLabel            = cms.InputTag("jetsAK4", "jetAK4jetArea"),
    AK4JetSelParams            = defaultAK4JetSelectionParameters.clone(),
    BTaggedAK4JetSelParams     = defaultBTaggedAK4JetSelectionParameters.clone(),
    AK8JetSelParams            = defaultAK8JetSelectionParameters.clone(),
    HJetSelParams              = defaultHJetSelectionParameters.clone(),
    WJetSelParams              = defaultWJetSelectionParameters.clone(),
    ak8jetsPtMin               = cms.double  (300),
    ak8jetsEtaMax              = cms.double  (2.4),
    ak4jetsPtMin               = cms.double  (30),
    ak4jetsEtaMax              = cms.double  (2.4),
    hltPaths                   = cms.vstring ("HLT_PFJet260_v1", "HLT_AK8PFJet360TrimMod_Mass30_v1", "HLT_PFHT900_v1"),
    TJetSelParams              = defaultTJetSelectionParameters.clone(),
    HTMin                      = cms.double  (300.),
    wmassmin                   = cms.double  (50.),
    wmassmax                   = cms.double  (100.),
    scaledmassdropmin          = cms.double  (0.),
    scaledmassdropmax          = cms.double  (0.5)
    )


process.TFileService = cms.Service("TFileService", fileName = cms.string('QCD500.root') )


process.p = cms.Path(process.presel*process.analyze)

#process.p = cms.Schedule(p2)

