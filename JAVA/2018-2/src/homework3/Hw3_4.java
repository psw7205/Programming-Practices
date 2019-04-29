package homework3;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class RandomJLabel extends JPanel implements MouseListener {
	JLabel l;

	RandomJLabel() {
		setLayout(null);
		l = new JLabel("c");
		int width2 = 10;
		l.setSize(width2, width2);
		l.setLocation(100, 100);
		add(l);
		addMouseListener(this);

	}

	@Override
	public void mouseClicked(MouseEvent arg0) {
		int x = (int) (Math.random() * 500);
		int y = (int) (Math.random() * 500);

		l.setLocation(x, y);
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {}

	@Override
	public void mouseExited(MouseEvent arg0) {}

	@Override
	public void mousePressed(MouseEvent arg0) {}

	@Override
	public void mouseReleased(MouseEvent arg0) {}

}

public class Hw3_4 extends JFrame {
	Hw3_4() {
		this.setTitle("클릭 연습 용 응용프로그램");
		this.setSize(500, 500);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);

		RandomJLabel p = new RandomJLabel();
		add(p);

		setVisible(true);
	}

	public static void main(String[] args) {

		new Hw3_4();
	}

}
