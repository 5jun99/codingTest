package asis;

import asis.controller.EvaluationController;
import asis.view.EvaluationView;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        EvaluationView view = new EvaluationView(sc);
        EvaluationController controller = new EvaluationController(view);
        controller.run();
    }
}