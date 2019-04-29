import javax.swing.JFrame;

public class GameFrame extends JFrame{
	public GameFrame() {
	this.setSize(800, 800);
	this.setTitle("Game of Life");
	this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	
	this.add(new PlayPanel());
	
	this.setVisible(true);
	}
	
	public static void main(String[] args) {
			new GameFrame();
	}

}
