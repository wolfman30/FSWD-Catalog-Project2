from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AgingHallmark

engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

genomic_instability = AgingHallmark(name="Genomic instability")
session.add(genomic_instability)
session.commit()

telomere_attrition = AgingHallmark(name="Telomere attrition")
session.add(telomere_attrition)
session.commit()

epigenetic_alterations = AgingHallmark(name="Epigenetic alterations")
session.add(epigenetic_alterations)
session.commit()

proteostasis_loss = AgingHallmark(name="Loss of proteostasis")
session.add(proteostasis_loss)
session.commit()

dereg_nutri_sensing = AgingHallmark(name="Deregulated nutrient sensing")
session.add(dereg_nutri_sensing)
session.commit()

mitochondrial_dysfunction = AgingHallmark(name="Mitochondrial dysfunction")
session.add(mitochondrial_dysfunction)
session.commit()

cellular_senescence = AgingHallmark(name="Cellular senescence")
session.add(cellular_senescence)
session.commit()

stem_cell_exhaustion = AgingHallmark(name="Stem cell exhaustion")
session.add(stem_cell_exhaustion)
session.commit()

altered_ic_comm = AgingHallmark(name="Altered intercellular communication")
session.add(altered_ic_comm)
session.commit()

print("Added aging hallmarks!")

#Aging Hallmarks from the article 'Hallmarks of Aging' here: 
                        #https://www.cell.com/action/showPdf?pii=S0092-8674%2813%2900645-4