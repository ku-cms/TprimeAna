import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_1.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_2.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_3.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_4.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_5.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_6.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_7.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_8.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/JetHT/crab_JetHT2015D-200/151020_205103/0000/PreselEvents_JetHT2015D-200_9.root'
    )
)

