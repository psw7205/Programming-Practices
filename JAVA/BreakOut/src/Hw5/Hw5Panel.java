package Hw5;

import java.awt.CardLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JPanel;

class Hw5Panel extends JPanel implements KeyListener {

	CardLayout card = new CardLayout();
	Hw5StartPanel start = new Hw5StartPanel();
	Hw5GamePlayPanel game = new Hw5GamePlayPanel();
	Hw5EndPanel end = new Hw5EndPanel();
	int idx = 0;

	Hw5Panel() {
		game.parent = this;
		setLayout(card);
		add(start, "start");
		add(game, "game");
		add(end, "end");
		addKeyListener(this);
		requestFocus();
		setFocusable(true);
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void keyPressed(KeyEvent e) {
		if (e.getKeyCode() == KeyEvent.VK_SPACE) {
			if (idx == 0) {
				idx = 1;
				card.show(this, "game");
				game.init();
				start.startClip.stop();
				setFocusable(false);
				return;
			}
			
			if(idx == 2)
			{
				idx = 0;
				card.show(this, "start");
				start.startClip.setFramePosition(0);
				start.startClip.start();
				return;
			}
		}
	}

	@Override
	public void keyReleased(KeyEvent e) {

	}

}
