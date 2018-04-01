"""Python challenge - 1st day
   name generator -app
   Allows to generate female or male name with last name."""

import random

female_name = ["MARY","PATRICIA", "LINDA", "BARBARA","ELIZABETH", "JENNIFER", "MARIA", "SUSAN", "MARGARET", "DOROTHY","LISA", "NANCY", "KAREN", "BETTY",	"HELEN",
          "SANDRA", "DONNA", "CAROL", "RUTH", "SHARON",	"MICHELLE",	"LAURA", "SARAH", "KIMBERLY", "DEBORAH", "JESSICA", "SHIRLEY", "CYNTHIA", "ANGELA",
          "MELISSA", "BRENDA", "AMY", "ANNA", "REBECCA", "VIRGINIA", "KATHLEEN", "PAMELA", "MARTHA", "DEBRA", "AMANDA", "STEPHANIE", "CAROLYN", "CHRISTINE",
          "MARIE", "JANET", "CATHERINE", "FRANCES", "ANN", "JOYCE", "DIANE", "ALICE", "JULIE",  "HEATHER", "TERESA","DORIS","GLORIA", "EVELYN", "JEAN",
          "CHERYL", "MILDRED",  "KATHERINE", "JOAN", "ASHLEY", "JUDITH", "ROSE", "JANICE", "KELLY", "NICOLE", "JUDY", "CHRISTINA", "KATHY", "THERESA",
          "BEVERLY", "DENISE", "TAMMY", "IRENE", "JANE", "LORI", "RACHEL", "MARILYN", "ANDREA", "KATHRYN", "LOUISE", "SARA", "ANNE", "JACQUELINE",
          "WANDA", "BONNIE", "JULIA", "RUBY", "LOIS", "TINA", "PHYLLIS", "NORMA", "PAULA", "DIANA"]

male_name = ["Jorge", "John", "Kade", "Kolten", "Bentley", "Jarrett", "Dax", "Devin","Connor", "Trevor", "Bruce", "Ivan", "Maximo", "Dallas", "Camren",
              "Desmond", "Davian", "Douglas", "Collin", "Brayden", "Clarence", "Jakobe", "Kellen", "Rory", "London", "Jamal", "Kai", "Isaias", "Clinton",
              "Troy", "Reed", "Marquise", "Logan", "Jaxon", "Ross", "Branden", "Alfonso", "Giovani", "Deandre", "Noe", "Terry", "Kasen", "Kameron",
              "Davion", "Seth", "Waylon", "Hugo", "Simeon", "Dillon", "Leo", "Mohammed", "King", "Brent", "Gustavo", "Boston", "Zack", "Izaiah", "Braydon",
              "Jaydon", "Darius", "Zackary", "Manuel", "Carsen", "Yosef", "August", "Glenn", "Jon", "Bryan", "Andreas", "Uriel", "Ahmad", "Gavin", "Nick",
              "Javier", "Easton", "Jerimiah", "Jakob", "Esteban", "Owen", "Pranav", "Marshall", "Gilbert", "Aden", "Xzavier", "Eliezer", "Marcel", "Gianni",
              "Valentin", "Bruno", "Aydin", "Jax", "Jadiel", "Dwayne", "Simon", "Jaylon", "Dustin", "Quinton", "Brian", "Denzel", "Randy", "Ricardo"]

last_name = ["Delgado", "Rosario", "Stevens", "Vasquez", "Bryan", "Garza", "Davenport", "Parks", "Perez", "Cabrera", "Grant", "Flowers", "Carson",
              "Morgan", "Diaz", "Nielsen", "Brock", "Horne", "Haynes", "Gallegos", "Anthony", "Roy", "Dillon", "Montgomery", "Meyers", "Barton", "Fowler",
              "Rowland", "Pierce", "Brennan", "Gordon", "Copeland", "Riley", "Cohen", "Bonilla", "Berger", "Hood", "Meadows", "Love", "Ruiz", "Hines",
              "Griffith", "Velez", "Ibarra", "Rhodes", "Wright", "Salazar", "Fuentes", "Marks",  "Hancock", "Robertson", "Christian", "Bauer",  "Deleon",
              "Grimes", "Haley", "Yu", "Roman", "Doyle", "Aguilar", "Graves", "Black", "Booth", "Cochran", "Arias", "Farrell", "Ross", "Gamble", "Leonard",
              "Chandler", "Hicks", "Montes", "Velasquez", "Ballard", "Bautista", "Livingston", "Curtis", "Kane", "Fry", "Fitzpatrick", "Fritz", "Lang",
              "Baldwin", "Foster", "Kemp", "Wyatt", "Liu", "Blevins", "Morse", "Frederick", "Wolfe", "Griffin", "Ortega", "Simmons", "Peters", "Maynard",
              "Orozco", "Krause", "Fitzgerald", "Lowe"]

print("Welcome to NAME GENERATOR. \nWould you like to generate female or male name?")


def user_name():
    while True:
        user_choice = input("Enter f for female or m for male: ")
        if user_choice == 'f' or user_choice == 'F':
            f_name = str("".join(random.choice(female_name) + " " + random.choice(last_name))).upper()
            print("Hello, " + f_name + ".")
            break
        if  user_choice == 'm' or user_choice == "M":
            m_name = str("".join(random.choice(male_name) + " " + random.choice(last_name))).upper()
            print("Hello, " + m_name + ".")
            break
        else:
            print("Sorry, I don't understand that.")

user_name()