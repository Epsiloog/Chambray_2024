import java.util.Objects;
import java.util.Scanner;

public class MainClass {
    public static char main(String[] args){
        String[][] r_c1_1 = {{"a) cellules semblables","b) cellules différentes","c) cellules sécrétrices","d) cellules jointives"},
                {"a) sont avasculaires", "b) sont toujours au contact du milieux extèrieur","c) peuvent constituer des glandes","d) sont constitués de cellules éparses"},
                {"a) l'épiderme","b) l'épithélium intestinal","c) l'épithélium pulmonaire","d) l'endothélium vasculaire"},
                {"a) sécrètent toutes des hormones","b) ont un rôle de sécrétation","c) sont parfois en relation avec le milieu extérieur","d) sont parfois d'origine épithéliale", "e) soit d'origine conjonctive"},
                {"a) ne sont jamais au contact du milieu extérieur","b) sont constituées de cellules jointives","c) sont constitués de cellules éparses","d) ne sont jamais vascularisés"}};
        String[] q_c1_1 = {"Tous les tissus épithéliaux renferment des :","Les tissus épithéliaux :","Les tissus suivants sont des épithéliums unistratifiés :","Les glandes :", "Les tissus conjonctifs :"};
        String[] Br_c1_1 = {"ad","ac","bcd","b","ac"};
        questionnaire C1_1 = new questionnaire(q_c1_1.length, r_c1_1,q_c1_1);
        System.out.println("Bienvenue dans ce questionnaire écrit en POO sur la biologie et la physiopathologie humaines !");
        System.out.println("Il y a 5 questions, chaque bonne réponse vous rapporte 1 point, 1 mauvaise réponse vous enlève 0.5 points");
        System.out.println("Lorsque vous pensez qu'il y a plusieurs réponses, écrivez les sous la forme : 'abc ...'\n");

        while(questionnaire.getQ_actuelle()<questionnaire.getNb_question()){
            System.out.println("Question n°"+(questionnaire.getQ_actuelle()+1)+"\n");
            System.out.println(q_c1_1[questionnaire.getQ_actuelle()]);
            for(int j=0;j<r_c1_1[questionnaire.getQ_actuelle()].length;j++)
                System.out.println(r_c1_1[questionnaire.getQ_actuelle()][j]);

            Scanner clavier = new Scanner(System.in);
            String reponse="";
            //if(clavier.hasNextLine())
            reponse = clavier.nextLine();

            if(Objects.equals(reponse, Br_c1_1[C1_1.getQ_actuelle()]))
                C1_1.bonne_reponse();
            else{
                C1_1.mauvaise_reponse();
                System.out.println("La bonne réponse était : " + Br_c1_1[C1_1.getQ_actuelle()]);
            }
            System.out.println("Votre score est de : " + C1_1.getScore() + "/5" + "\n");
            C1_1.questionsuivante();
        }
        System.out.println("Quiz terminé !  Votre score final est de : " + C1_1.getScore() + "/5");
    }
}
