package homework3;

import java.awt.Font;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class KeyShift extends JPanel implements KeyListener {

	JLabel l;

	KeyShift() {
		l = new JLabel("Love Java ");
		l.setFont(new Font("Arial", Font.PLAIN, 30));
		add(l);

		this.setFocusable(true);
		this.requestFocus();
		this.addKeyListener(this);
	}

	@Override
	public void keyPressed(KeyEvent e) {
		if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			String firstChar = l.getText().substring(0, 1);
			String str = l.getText().substring(1);

			l.setText(str + firstChar);

		}

	}

	@Override
	public void keyReleased(KeyEvent e) {}

	@Override
	public void keyTyped(KeyEvent e) {}

}

public class Hw3_3 extends JFrame {
	public Hw3_3() {
		setTitle("Left 키로 문자열 이동");
		setSize(500, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		KeyShift p = new KeyShift();
		add(p);

		setVisible(true);
	}

	static public void main(String[] args) {
		new Hw3_3();
	}
}
