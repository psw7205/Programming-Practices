import java.awt.Graphics;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JPanel;

public class PlayPanel extends JPanel implements Runnable {

	static final int cols = 70;
	static final int rows = 70;
	static final int offset = 10;
	int grid[][] = new int[rows][cols];

	PlayPanel() {

		makeRandomArray();

		Thread t = new Thread(this);
		t.start();
	}

	@Override
	public void run() {
		while (true) {
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			nextGeneration();
			repaint();
		}
	}

	void makeRandomArray() {
		for (int i = 0; i < rows; ++i) {
			for (int j = 0; j < cols; ++j) {
				grid[i][j] = (int) (Math.random() * 2);
			}
		}
	}

	void nextGeneration() {
		int next[][] = new int[rows][cols];

		for (int i = 1; i < rows - 1; ++i) {
			for (int j = 1; j < cols - 1; ++j) {
				int state = grid[i][j];
				int neighbors = 0;

				for (int x = -1; x < 2; ++x) {
					for (int y = -1; y < 2; ++y) {
						neighbors += grid[i + x][j + y];
					}
				}

				neighbors -= state;

				if (state == 0 && neighbors == 3) {
					next[i][j] = 1;
				} else if (state == 1 && neighbors < 2) {
					next[i][j] = 0;
				} else if (state == 1 && neighbors > 3) {
					next[i][j] = 0;
				} else {
					next[i][j] = state;
				}
			}

		}

		grid = next;
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		for (int i = 0; i < rows; ++i) {
			for (int j = 0; j < cols; ++j) {
				int x = i * 10 + offset;
				int y = j * 10 + offset;

				if (grid[i][j] == 0)
					g.drawRect(x, y, 10, 10);
				else if (grid[i][j] == 1)
					g.fillRect(x, y, 10, 10);
			}
		}
	}
}
