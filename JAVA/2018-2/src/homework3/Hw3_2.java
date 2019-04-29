package homework3;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Hw3_2 extends JFrame {

	Hw3_2() {
		setTitle("계산기 프레임");
		setSize(400, 300);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel buttonPanel = new JPanel();
		buttonPanel.setLayout(new GridLayout(4, 4));
		JButton tmp[] = new JButton[16];

		for (int i = 0; i < 10; i++) {
			String str = i + "";
			tmp[i] = new JButton(str);
			buttonPanel.add(tmp[i]);
		}

		tmp[10] = new JButton("CE");
		tmp[11] = new JButton("계산");
		tmp[12] = new JButton("+");
		tmp[13] = new JButton("-");
		tmp[14] = new JButton("x");
		tmp[15] = new JButton("/");

		for (int i = 0; i < 4; i++) {
			tmp[i + 12].setBackground(Color.CYAN);
		}

		for (int i = 0; i < 6; i++) {
			buttonPanel.add(tmp[10 + i]);
		}

		JPanel topPanel = new JPanel();
		JLabel text1 = new JLabel("수식입력");
		JTextField in = new JTextField(30);
		topPanel.setBackground(Color.LIGHT_GRAY);
		topPanel.add(text1);
		topPanel.add(in);

		JPanel resultPanel = new JPanel();
		JLabel text2 = new JLabel("계산결과");
		JTextField out = new JTextField(30);
		resultPanel.setBackground(Color.YELLOW);
		resultPanel.add(text2);
		resultPanel.add(out);

		add(topPanel, BorderLayout.NORTH);
		add(buttonPanel, BorderLayout.CENTER);
		add(resultPanel, BorderLayout.SOUTH);

		setVisible(true);

	}

	public static void main(String[] args) {
		new Hw3_2();

	}

}
