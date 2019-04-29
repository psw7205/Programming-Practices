package homework3;

import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Hw3_1 extends JFrame {

	Hw3_1() {
		setTitle("Ten Color Buttons Frame");
		setSize(1000, 400);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel p = new JPanel();
		p.setLayout(new GridLayout(1, 10));
		JButton tmp[] = new JButton[10];

		for (int i = 0; i < 10; i++) {
			String str = i + "";
			tmp[i] = new JButton(str);
			p.add(tmp[i]);
		}

		tmp[0].setBackground(Color.RED);
		tmp[1].setBackground(Color.ORANGE);
		tmp[2].setBackground(Color.YELLOW);
		tmp[3].setBackground(Color.GREEN);
		tmp[4].setBackground(Color.CYAN);
		tmp[5].setBackground(Color.BLUE);
		tmp[6].setBackground(Color.MAGENTA);
		tmp[7].setBackground(Color.LIGHT_GRAY);
		tmp[8].setBackground(Color.DARK_GRAY);
		tmp[9].setBackground(Color.PINK);

		add(p);
		setVisible(true);

	}

	public static void main(String[] args) {
		new Hw3_1();
	}
}
