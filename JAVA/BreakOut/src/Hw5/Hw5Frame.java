package Hw5;

import javax.swing.JFrame;

public class Hw5Frame extends JFrame {

	Hw5Frame() {
		this.setTitle("java Hw5 - 16013093 ¹Ú»ó¿ì");
		this.setSize(800, 800);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setResizable(false);
		
		Hw5Panel p = new Hw5Panel();
		add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Hw5Frame();
	}

}
