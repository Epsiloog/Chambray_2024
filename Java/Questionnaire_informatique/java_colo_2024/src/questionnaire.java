// création d'une classe questionnaire avec les attributs privés et public ainsi que les modificateurs suivants :
public class questionnaire {
    private static int q_actuelle;
    private static int nb_question;
    private final String[][] reponses;
    private final String[] questions;
    private double score;

    // constructeur
    public questionnaire(int nb_question, String[][] reponses,String[] questions){
        q_actuelle=0;
        questionnaire.nb_question = nb_question;
        this.reponses=reponses;
        this.questions=questions;
        this.score=0;
    }

    // méthodes utiles au déroulement du questionnaire
    static int getQ_actuelle(){
        return q_actuelle;
    }
    static int getNb_question(){
        return nb_question;
    }

    public double getScore() {
        return score;
    }

    static void questionsuivante(){
        q_actuelle++;
    }
    void bonne_reponse(){
        System.out.println("\nBonne réponse !");
        this.score++;
    }
    void mauvaise_reponse(){
        if(getScore()>0)
            this.score=this.score-0.5;
        System.out.println("\nMauvaise réponse !");
    }
}