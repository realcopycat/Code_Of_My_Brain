from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://MyBrain:7687",auth=("copycat","0311"))

def writeInMyMemory(Memory,count):

    #execute Cypher script
    Memory.run("MATCH (a:Person {name:'Me'})-[r1:adore {How_many_times_do_I_miss_you_every_day: $number1}]->(b:Girl {Favorite_flower:babysbreath})"
               "DELETE r1"
               "CREATE (a)-[r2:adore {How_many_times_do_I_miss_you_every_day: $number2}]->(b)",
               number1=count-1,number2=count)

while(when_I_wake_up_at_6_am):

    if you_have_not_respond_to_me:

        count += 1
        with driver.session() as session:

            try:
                session.write_transaction(writeInMyMemory,count)
            except:
                print("I wish I don't know you.")

                print("But I do.")
                count += 1

    elif you_feel_same_with_me:

        import math
        count=exp(count)