import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/5E2A0DB9-E52F-E511-A294-782BCB407B74.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/8CD2F9D4-F031-E511-9CB9-782BCB282C03.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/B26E1B1D-3634-E511-A358-00261894384F.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/C0199F1C-3634-E511-923D-0025905A60CA.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/D6E2921C-3634-E511-8BEA-0025905B860E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/DE7BBF31-2233-E511-B96B-0CC47A13D2A4.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/E489D8AB-9630-E511-8829-782BCB20F01D.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/F2801823-3634-E511-B971-002354EF3BE1.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/F8789F1B-3634-E511-B83C-0025905A60B2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/FE3F2F1E-3634-E511-9A73-002618943870.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/0063D273-F92F-E511-A9C2-90B11C27F8B2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/00C3C3F5-BF2C-E511-BDF5-AC853D9F5120.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/0251EFFD-022B-E511-BD6D-001E6878F905.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/02859AF8-FB2F-E511-8A60-002590E2F65E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/029F5FD6-AB2C-E511-8BE0-0002C90A3560.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/02B77B78-0E2B-E511-A0C2-B083FED76DA5.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/04768B71-F92F-E511-A61F-0CC47A13D16A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/08D181BD-182E-E511-8AB6-0026B95CD6D9.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/0A5A8079-F92F-E511-88C8-0025904A8ECA.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/1041CC2E-1F30-E511-8CB8-0025901AC3C6.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/12F9AAA0-FB2F-E511-9955-0CC47A13D2A4.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/146BC89E-4D2B-E511-8BC8-000F530E47E0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/1646486E-F92F-E511-9EF5-0CC47A13CD44.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/164D5760-792F-E511-8101-002590D4FC42.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/18768C51-BA2E-E511-9DF9-0025905A6126.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/1891E9BC-072B-E511-93A9-000F530E4774.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/1A2C36B1-1A2B-E511-8FD8-AC853D9F5344.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/1CE7203F-0D2B-E511-AED5-AC853DA06B56.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/2002D575-F92F-E511-94B5-90B11C2AB44B.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/204D3719-212B-E511-A0CB-B083FED7477A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/20550575-F92F-E511-AD5A-0CC47A13CCFC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/26856C29-492F-E511-A34C-B083FED764C0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/26FDB53D-BA2E-E511-A02C-0025905A6084.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/2AC37190-F92F-E511-B49D-0CC47A13D216.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/2E54DD3E-BA2E-E511-95A6-0025905A60B2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/32BD3627-1430-E511-895F-6CC2173BBE70.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/32F2E95A-0C2B-E511-905F-782BCB6E134C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/34F27E96-BD2E-E511-8E87-0025905B8572.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/3E8A8F6F-F92F-E511-8EE9-002590E2F65E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/40EB12C1-182E-E511-89F5-782BCB27C5C0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/4AE52374-F92F-E511-8DEB-0025907253E0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/4CDC5FF9-022B-E511-9E63-842B2B2AB674.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/5477115B-FC2F-E511-9A02-0025904AC2CC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/5C39ED3F-032B-E511-A099-AC853D9DACE1.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/600A7E4F-FC2F-E511-BEA6-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/60B2935F-FC2F-E511-8BA7-002590489776.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/6A852918-BB2C-E511-9453-D4AE526A1687.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/6CE9C73B-032B-E511-A3A1-000F532734B4.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/70ACE975-F92F-E511-B8FA-003048F5ADF8.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/723C0C71-F92F-E511-B242-002590E39D52.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/723D310A-EC2D-E511-8A6C-001EC9B218A8.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/725EB859-FC2F-E511-9A9D-0025904897C2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/74148638-102B-E511-9201-AC853D9F5344.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/76FB44B6-F92F-E511-A75F-002590E2F9D4.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/78F252BD-932D-E511-8B37-008CFA151F98.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/7A405279-F92F-E511-AA9C-003048F5970A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/7A670668-0C2B-E511-AB33-001E68862A32.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/7C707F94-172E-E511-ABAB-001E68865F6C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/80198A71-F92F-E511-A6F7-0CC47A13D16A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/88923319-D92D-E511-98FA-0002C90F8088.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/88B2A651-FC2F-E511-A1FC-0CC47A13CCFC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/8C6D326C-5B2F-E511-9E6A-0025905B857C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/8EC0C168-AF2C-E511-B4CC-008CFA1CBA20.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/90060B5F-FC2F-E511-B7D9-0CC47A13CB62.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/92A9449B-B22C-E511-9220-0026B9278678.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/985415C1-182E-E511-A7F6-782BCB27C5C0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/9AB31F07-FC2F-E511-8E6A-002590E2DD10.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/9CD18970-F92F-E511-9074-002590E2DD10.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/9CE8F7CC-DF2B-E511-B364-02163E011955.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/A6EEBFAF-0730-E511-A0D9-A0040420FE80.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/A8625E96-BD2E-E511-8148-0025905A60D0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/AC80F952-FC2F-E511-9BB2-002590E3A024.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/ACF65FF3-262E-E511-8D32-842B2B185C54.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/AE27D67A-F92F-E511-BCA2-003048F5B2A6.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/BAAE9914-092B-E511-8526-000F53273500.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/BE371290-472F-E511-B6B4-0026B95BE32C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C03C8E6E-F92F-E511-8A89-0CC47A13CD44.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C0E08493-BD2E-E511-AD52-0025905964BE.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C2F8C8C6-182E-E511-99B9-782BCB281FC8.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C4BB2F58-BA2E-E511-84C9-0025905B858A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/C6B09C6D-F92F-E511-BFB3-0CC47A13D2A4.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/CACD1880-F92F-E511-A3DE-003048F5B6B0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/CCCBEA5A-FC2F-E511-853F-0025904886E6.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/CCE85FF9-022B-E511-87E9-842B2B2A7CF2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/DC946A19-BB2C-E511-B9D6-001EC9AF22AD.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/DC985167-AF2C-E511-AE41-008CFA197EB0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/DEBD9A72-F92F-E511-BBBF-0025907253D2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/E839FA08-052B-E511-B076-842B2B2B0DAD.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/E85CDCB1-1A2B-E511-99B6-000F530E46B0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/E8EBC3B9-472F-E511-8606-001E6878F9C1.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/EA5328C1-182E-E511-90F9-001E688629D2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/EAA21B54-4C2F-E511-AC7D-001E6849D24B.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/EC0D3214-BB2C-E511-9A20-D4AE526A023A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/F079143F-0D2B-E511-871B-AC853D9DAC25.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/F2C8D6FB-BB2E-E511-90AF-0025905A6134.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/F62A2644-032B-E511-BECC-782BCB407BCB.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/F6AD5A73-F92F-E511-936F-002590E2D9FE.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/F6D23333-182B-E511-8D7F-0025905B855C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/FA4DF778-F92F-E511-BB34-0025901D0946.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/FC9100C6-182E-E511-B07D-782BCB408BD2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/FC930B93-5B2F-E511-8104-D48564593F64.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/FC98EAE8-022B-E511-9191-B083FED76DBD.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/FED1CB2D-3330-E511-A1B3-0025905A60D6.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/FED23903-0D2B-E511-BE17-842B2B185C51.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/02219C5D-523B-E511-874C-0025900B5648.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/0805C29D-523B-E511-AF2B-0025901D16AC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/089137DA-482F-E511-992C-A4BADB0F5175.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/08E70AC0-B431-E511-97D5-002590550516.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/0CC0BB7F-462F-E511-8C36-842B2B2B0E64.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/12355BD9-523B-E511-9813-0002C90F8088.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/1268AC7B-5C2E-E511-AAE8-68B5996BD98E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/1AEB9D64-5D2C-E511-A31B-AC853D9DACD7.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/1E1A7FF0-602E-E511-80DB-002481CFE642.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/22AC948D-7C33-E511-9B34-000F53273730.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/2804BF76-5D2C-E511-A133-001E688651D4.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/2CC1F97F-5D2C-E511-BB04-B083FED76DBD.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/2E336A74-523B-E511-B738-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/32EEDA5C-5D2C-E511-B057-000F530E4794.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/363196A6-1A2D-E511-AAAC-001E67A406E0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/3AC413AB-362F-E511-AD14-3417EBE64BAF.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/4268A391-462F-E511-AD33-782BCB27F1F0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/42887478-5D2C-E511-B178-000F53273740.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/4480BF93-612C-E511-B61B-000F53273734.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/48832B2B-5F2E-E511-BFA6-002481CFE1EC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/4E4A4D54-462F-E511-8ADF-AC853D9F5256.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/52C0EE14-9031-E511-BEE9-00266CFAE854.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/54126A07-972C-E511-9383-B8CA3A70A5E8.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/5858FE81-523B-E511-BCA5-0CC47A0AD6FE.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/58CAE66C-5D2C-E511-95F5-B083FED76C6C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/5A57F682-462F-E511-88BC-000F53273734.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/5AF6658E-612C-E511-8BC0-000F53273750.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/604BF0DA-523B-E511-97FB-842B2B18240B.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/66140F56-462F-E511-9AD3-782BCB27F1F0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/66C0C76E-5D2C-E511-807F-AC853D9DACD7.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/6EF87639-852C-E511-AFB7-B8CA3A70A410.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/7002CDA8-732B-E511-AACB-90B11C04FE0C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/7221EE4F-523B-E511-99BF-90B11C26815F.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/72E07071-612D-E511-A2C4-A0369F3102B6.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/74014893-482F-E511-A548-000F532734AC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/76CE2269-462F-E511-A43C-782BCB27BA01.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/9639A588-5D2C-E511-B9D0-782BCB6E1220.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/9653DD96-523B-E511-BA3D-0CC47A13D284.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/96611650-523B-E511-AD06-0CC47A13CCEE.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/A498E559-523B-E511-928A-002590489776.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/AA18FCAB-782B-E511-B2F3-F45214CEF24A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/B2BEF399-523B-E511-A95D-002590E3A286.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/BA16502E-5F2E-E511-AB8E-90B11CBCFF68.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/CCD13157-523B-E511-859C-00238BBD75D6.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/CE2691D4-482F-E511-A65E-842B2B298D4E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/DCA1DE00-742E-E511-B7FE-000F53273738.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/DCB61C03-742E-E511-9986-001E6878F8B9.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/DE8964F2-392F-E511-A85E-3417EBE6453D.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/DEE5B02C-6B2F-E511-8743-0025905B858A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E469BA2A-6B2F-E511-BCF5-0025905A609A.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E8C0A68C-7C33-E511-B671-0026B95C188C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/EACDE8DF-523B-E511-909A-842B2B1858F2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/ECFCE2C6-752E-E511-818C-0026B95ADB18.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/EE2C1F24-5F2E-E511-823A-0015C5F83096.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F260595B-462F-E511-906C-000F532734A0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F645889D-802C-E511-85B2-00259021A2AA.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F6DCB7E1-523B-E511-9CAE-842B2B185C51.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F82F19AB-7E30-E511-81D3-78E7D1E4AF92.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/FC4DA9FE-DD2A-E511-953C-0025905C3E68.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/FC63476B-523B-E511-8121-0025901AFEA2.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/18B58378-CC32-E511-B195-6C3BE5B5A4C8.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/1E5BAAE8-1B32-E511-B23C-002590DB923C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/24754E0B-A233-E511-99E3-000F5327372C.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/24C6185F-E733-E511-8570-0025905A6084.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/4ABAF75B-E733-E511-80C8-0025905A608E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/6020AFC8-E733-E511-814C-00221982C606.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/6A33892B-C632-E511-81A2-842B2B18240B.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/703240D8-EB2B-E511-983A-002481CFE25E.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/824F1331-C632-E511-9F2C-842B2B185C51.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/9CF15DA9-0F33-E511-9429-00266CFAE788.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/A2649402-1C32-E511-B939-002481E0D678.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/B64F8318-1233-E511-9A80-0025907DC9C0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/CCB24034-E733-E511-8C20-002590D9D8BC.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/D2E6BF01-A233-E511-B750-000F53273728.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/DA844E2C-C632-E511-9FE5-001E6849D21B.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/E097B444-E733-E511-8949-0CC47A13CB36.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/F08EF617-1233-E511-834E-0025907DC9C0.root',
       '/store/mc/RunIISpring15DR74/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/80000/F2805EE5-1B32-E511-B14F-E41D2D08DF80.root' ] );


secFiles.extend( [
               ] )
