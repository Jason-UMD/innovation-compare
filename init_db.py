import psycopg2
import db_helpers as db

conn, cur = db.get_db_connection()
with open('schema.sql') as f:
    cur.execute(f.read())
db.close_db_connection(conn)

db.create_topic('Advanced Gas Turbine Engine',
        ['10.1038/nmat4687',
        '10.1016/j.paerosci.2017.08.001',
        '10.1016/j.apenergy.2017.04.048',
        '10.2514/1.J055361',
        '10.1016/j.ijhydene.2019.12.143'], [])
        
db.create_topic('Advanced Manufacturing',
        ['10.1016/j.pmatsci.2017.10.001',
        '10.1016/j.compositesb.2018.02.012',
        '10.1016/j.compositesb.2016.11.034',
        '10.1016/J.ENG.2017.05.015',
        '10.1126/science.aai7899'], [])
        
db.create_topic('Financial Technologies',
        ['10.1109/MC.2017.3571064',
        '10.1016/j.elerap.2019.100833',
        '10.1108/IMDS-08-2018-0368',
        '10.1016/j.jsis.2018.10.002',
        '10.1109/BigDataCongress.2017.85'], [])
        
db.create_topic('Advanced Nuclear Energy Technologies',
        ['10.1016/j.pmatsci.2019.01.005',
        '10.1039/C8TA09486A',
        '10.1016/j.jclepro.2018.05.271',
        '10.1016/j.jclepro.2018.01.262',
        '10.1016/j.apenergy.2018.03.002'], [])
        
db.create_topic('Microelectronics',
        ['10.1038/s41586-018-0028-z',
        '10.1038/s41586-018-0028-z',
        '10.1038/nphoton.2017.75',
        '10.1038/s41551-018-0335-6',
        '10.1038/s41928-020-0461-5'], [])
        
db.create_topic('Renewable Energy Generation and Storage',
        ['10.4324/9780203790434',
        '10.1021/acsami.5b09515',
        '10.1038/nmat4766',
        '10.1186/s12934-018-0879-x',
        '10.1021/jacs.8b04546'], [])
        
db.create_topic('Trusted AI and Autonomy',
        ['10.1038/nature14539',
        '10.1038/nature24270',
        '10.1109/TNNLS.2016.2582924',
        '10.1109/JPROC.2017.2761740',
        '10.1145/3298981'], [])
        
db.create_topic('Space Technology',
        ['10.1093/mnras/stx721',
        '10.1051/0004-6361/201832727',
        '10.1103/PhysRevLett.121.111302',
        '10.1093/MNRAS/STX2183',
        '10.1093/mnras/stw2805'], [])
        
db.create_topic('Human-Machine Interfaces',
        ['10.1002/adfm.201504755',
        '10.1038/nature25494',
        '10.1038/s41467-017-02685-9',
        '10.1126/sciadv.1700694',
        '10.1021/acsnano.8b02477'], [])
        
db.create_topic('Advanced Computing and Software',
        ['10.1038/s41592-019-0686-2',
        '10.1137/141000671',
        '10.1016/j.future.2019.02.028',
        '10.1016/j.agsy.2017.01.023',
        '10.1080/23746149.2016.1259585'], [])
        
db.create_topic('Integrated Network Systems-of-Systems',
        ['10.1109/JSAC.2019.2906789',
        '10.1109/MIE.2017.2649104',
        '10.1109/COMST.2017.2705720',
        '10.1109/MCOM.2017.1600863',
        '10.1007/978-981-10-5861-5_5'], [])
        
db.create_topic('Future Generation Wireless Technology',
        ['10.1109/JIOT.2018.2887086',
        '10.1007/s11432-020-2955-6',
        '10.1109/MCOM.2017.1500657CM',
        '10.1109/TWC.2019.2936025',
        '10.1109/MNET.001.1900287'], [])
        
db.create_topic('Biotechnology',
        ['10.1039/c8cs00457a',
        '10.1039/c7cs00240h',
        '10.1016/j.arabjc.2015.11.015',
        '10.1038/s41467-018-04252-2',
        '10.1126/science.aaq0180'], [])
        
db.create_topic('Quantum Science',
        ['10.1103/RevModPhys.89.035002',
        '10.1038/s41586-019-1666-5',
        '10.1126/science.abe8770',
        '10.1103/RevModPhys.90.015002',
        '10.1126/sciadv.abn5130'], [])
        
db.create_topic('Advanced Materials',
        ['10.1021/ja201269b',
        '10.1002/adma.201802981',
        '10.1002/adma.201703779',
        '10.1016/j.apenergy.2018.12.018',
        '10.1016/j.est.2019.100852'], [])
        
db.create_topic('Hypersonics',
        ['10.1146/annurev-fluid-122316-045217',
        '10.1016/j.jmst.2016.08.004',
        '10.1109/TIE.2019.2892696',
        '10.1109/TIE.2017.2701776',
        '10.1016/j.ijheatmasstransfer.2018.05.013'], [])
        
db.create_topic('Directed Energy',
        ['10.1016/B978-0-08-100433-3.00013-0',
        '10.3847/2041-8213/aa8f41',
        '10.1021/acs.chemrev.6b00468',
        '10.1080/24725854.2017.1417656',
        '10.1016/j.jmatprotec.2018.08.041'], [])
        
db.create_topic('Integrated Sensing and Cyber',
        ['10.1038/s41928-020-00501-9',
        '10.1007/s10163-018-0720-y',
        '10.1007/978-981-10-7901-6_89',
        '10.1109/JSEN.2020.2998168',
        '10.1109/COMST.2021.3122519'], [])
