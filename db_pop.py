from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AgingHallmark, HallmarkDetails, GlossaryofTerms, References

engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


genomic_instability = AgingHallmark(name="Genomic instability",
                                    summary = '''Endogenous and exogenous threats to the DNA 
                                                inside the nucleus and mitochrondria''', 
                                    treatment = '''Elimination of cells with the damanged DNA via apoptosis 
                                                and/or artificial reinforcement of DNA repair mechanisms''')
session.add(genomic_instability)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark=genomic_instability)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = genomic_instability)
session.add(detail2)
session.commit()


telomere_attrition = AgingHallmark(name="Telomere attrition", 
                                   summary = '''From normal cell divsion the gradual 
                                                reduction of the compound nucleotide 
                                                structures on the ends of chromosomes that 
                                                prevent chromosomal deterioration or fusion 
                                                with other chromosomes''', 
                                   treatment = 'Systemic viral transduction')
session.add(telomere_attrition)
session.commit()

detail1 = HallmarkDetails(name = 'Shelterin', 
                          description = '''multiprotein complex that binds telomeres together and protects telomeres
                                        from DNA repair mechanisms''',  
                          references = 'Bitchin ass sources!', 
                          aging_hallmark=telomere_attrition)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = telomere_attrition)
session.add(detail2)
session.commit()

epigenetic_alterations = AgingHallmark(name="Epigenetic alterations",
                                       summary = '''Changes to the expression of the genes in the DNA, 
                                                    but not the sequence or structure 
                                                    of the DNA can harm the body and accelerate aging ''')
session.add(epigenetic_alterations)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark=epigenetic_alterations)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = epigenetic_alterations)
session.add(detail2)
session.commit()

proteostasis_loss = AgingHallmark(name="Loss of proteostasis", 
                                  summary = '''The demise of the mechanisms that maintain 
                                            correct protein folding and break down of proteins, 
                                            or impairment of protein homeostasis (proteostasis)''')
session.add(proteostasis_loss)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!',
                          aging_hallmark = proteostasis_loss)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!',
                          aging_hallmark = proteostasis_loss)
session.add(detail2)
session.commit()

dereg_nutri_sensing = AgingHallmark(name="Deregulated nutrient sensing", 
                                    summary =  '''A pathways of cascading chemical interactions 
                                                for each unique fuel type in human cells is 
                                                not entirely clean and incurs long-term cost in the body''')
session.add(dereg_nutri_sensing)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = dereg_nutri_sensing)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = dereg_nutri_sensing)
session.add(detail2)
session.commit()

mitochondrial_dysfunction = AgingHallmark(name="Mitochondrial dysfunction", 
                                          summary = ''' Mitcochondria are the 'powerhouses' of the cell that convert food 
                                                    to a useful form called adenosine triphosphate (ATP). 
                                                    There are several ways for these organelles to malfunction. ''')
session.add(mitochondrial_dysfunction)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = mitochondrial_dysfunction)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = mitochondrial_dysfunction)
session.add(detail2)
session.commit()

cellular_senescence = AgingHallmark(name="Cellular senescence", 
                                    summary = '''Cellular senescence occurs when cells stop 
                                                dividing as they should. But the evidence of 
                                                their effect on the aging process is not well understood.''', 
                                    treatment = 'senolytics')
session.add(cellular_senescence)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = cellular_senescence)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = cellular_senescence)
session.add(detail2)
session.commit()

stem_cell_exhaustion = AgingHallmark(name="Stem cell exhaustion", 
                                     summary = '''The inability of stem cells to replenish 
                                                tissues and organs with functional specialized cells
                                                contributes to the malfunction of these tissues and organs. ''')
session.add(stem_cell_exhaustion)
session.commit()

detail0 = HallmarkDetails(name = 'Two Types of DNA', 
                          description = '(A) Nuclear DNA (B) Mitochondrial DNA')
session.add(detail0)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = stem_cell_exhaustion)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = stem_cell_exhaustion)
session.add(detail2)
session.commit()

altered_ic_comm = AgingHallmark(name="Altered intercellular communication", 
                                summary = '''Signaling between cells, over time, 
                                           will increase in self-preserving signals, 
                                           which damages the surrounding tissues''')
session.add(altered_ic_comm)
session.commit()

detail1 = HallmarkDetails(name = 'Endogenous threats', 
                          description = '''Reactive Oxygen Species(ROS), 
                                        DNA replication errors, spontaneous reactions''', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = altered_ic_comm)
session.add(detail1)
session.commit()

detail2 = HallmarkDetails(name = 'Exogenous threats', 
                          description = 'Chemicals, Radiation: Ultraviolet & Infrared', 
                          references = 'Bitchin ass sources!', 
                          aging_hallmark = altered_ic_comm)
session.add(detail2)
session.commit()

dna = GlossaryofTerms(name='deoxyribonucleic acid (DNA)', 
                      definition = '''double-stranded helix-shaped molecule in the nucleus and mitochondria of every human cell
                                     commonly known as the "blueprint" of life since it contains the instructions for building all proteins
                                    and enzymes used to produce all bodily structures and functions''')
session.add(dna)
session.commit()

genome = GlossaryofTerms(name='genome', 
                        definition = '''the entire genetic material of the organism: the entire sequence of genes composing
                                        the DNA both inside the nucleus of every cell and 
                                        in the mitochondria. Genomic instability refers to the 
                                        damage to and alterations of this genetic material.''')
session.add(genome)
session.commit()

exogenous_threats = GlossaryofTerms(name='exogenous threats', 
                                    definition = '''threats arising from outside or external to the genome.
                                                    The sun's ultraviolat rays (UV) and infrared radiation (IR).''')
session.add(exogenous_threats)
session.commit()

endogenous_threats = GlossaryofTerms(name = 'endogenous threats', 
                                     definition = '''threats to the genome that arise inside the nuclei 
                                                     or mitochondria''')
session.add(endogenous_threats)
session.commit()

reference1 = References(name = "[1] Hallmarks of Aging")
session.add(reference1)
session.commit()

reference2 = References(name = "[2] The Impact of Extracellular Matrix Proteins on the Aging Process")
session.add(reference2)
session.commit()

print("Added aging hallmarks!")

#Aging Hallmarks from the article 'Hallmarks of Aging' here: 
                        #https://www.cell.com/action/showPdf?pii=S0092-8674%2813%2900645-4