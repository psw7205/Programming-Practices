import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JPanel;

class GraphicsPanel extends JPanel implements MouseListener, MouseMotionListener {

	ArrayList<Point> sp;
	ArrayList<Point> ep; // 여러개 선을 그리기 위한 포인트 리스트

	int sx, sy, ex, ey;
	boolean lButton = false;

	GraphicsPanel() {
		this.addMouseListener(this); // 마우스리스너를 등록
		this.addMouseMotionListener(this);
		sp = new ArrayList<Point>();
		ep = new ArrayList<Point>();
	}

	// 필요할때마다 자동으로 호출
	@Override
	protected void paintComponent(Graphics g) {

		super.paintComponent(g); // 부모 클래스의 함수를 먼저 부르고 시작 (부모 클래스의 함수를 바꿔치기 때문에 없으면 문제가 생길 수 있음)
		
		// draw함수는 선만, fill은 색을 채워서 그림
		int w = this.getWidth();
		int h = this.getHeight(); // 화면 크기를 얻어 설정

		// int[] x = { 150, 100, 150, 200};
		int[] x = { w / 2, 0, w / 2, w };
		// int[] y = { 50, 100, 150, 100};
		int[] y = { 0, h / 2, h, h / 2 };
		g.setColor(Color.RED);
		g.fillPolygon(x, y, 4); // 화면의 꽉차는 마름모

		Color c = new Color(255, 0, 0); // RGB값을 생성자의 파라미터로 받음
		g.setColor(c); // 그리는 펜의 색을 설정
		g.drawRect(100, 100, 300, 200); // 100, 100을 시작점으로 가로로 300, 세로로 200 크기의 사각형

		g.setColor(Color.CYAN); // RED, GREEN, BLUE, BLACK, WHITE, GRAY, MAGENTA, CYAN, YELLOW ... 이미 상수값으로
								// 정해져있는 색들
		g.drawLine(100, 100, 300, 200); // 시작점과 끝점

		g.setColor(Color.BLACK);
		g.drawOval(100, 100, 300, 200); // 이 사각형을 채우는 원

		g.setColor(Color.MAGENTA);
		g.drawRoundRect(100, 100, 300, 200, 50, 50); // 사각형인데 모서리가 둥근 사각형

		g.setColor(Color.ORANGE);
		g.setFont(new Font("궁서체", Font.ITALIC, 30));// 폰트설정
		g.drawString("세종대학교", 100, 100); // 기준점 바로 위에 나타남
		g.setColor(Color.WHITE);
		g.drawString("세종대학교", 98, 98);

		g.setColor(Color.BLACK);
		//g.drawLine(sx, sy, ex, ey);
		

		for(int i = 0; i < sp.size(); i++)
		{
			Point s = sp.get(i);
			Point e = ep.get(i);
			g.drawLine(s.x, s.y, e.x, e.y);
		}
		
	}

	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseEntered(MouseEvent arg0) {

	}

	@Override
	public void mouseExited(MouseEvent arg0) {

	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		if (arg0.getButton() == MouseEvent.BUTTON1) {
			//sx = arg0.getX();
			//sy = arg0.getY();
			
			Point p1 = new Point(arg0.getX(), arg0.getY());
			Point p2 = new Point(arg0.getX(), arg0.getY());
			
			sp.add(p1);
			ep.add(p2);
			lButton = true;
		}
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		if (arg0.getButton() == MouseEvent.BUTTON1) {
			//ex = arg0.getX();
			//ey = arg0.getY();
			
			Point p = ep.get(ep.size()-1);
			p.x = arg0.getX();
			p.y = arg0.getY(); // 자바는 레퍼런스이기 때문에 데이터를 바꿔야함 
			
			lButton = false;
			this.repaint(); // 다시 그려야한다고 요청
		}
	}

	@Override
	public void mouseDragged(MouseEvent arg0) {
		if (lButton == true) { // flag변수를 둬 버튼 확인
			//ex = arg0.getX();
			//ey = arg0.getY();
			
			Point p = ep.get(ep.size()-1);
			p.x = arg0.getX();
			p.y = arg0.getY();
			this.repaint(); // 다시 그려야한다고 요청
		}
	}

	@Override
	public void mouseMoved(MouseEvent arg0) {

	}
}

// 그림은 뒤에서 부터 그려짐 프레임 -> 패널 순
// 윈도우가 프레임에게 그리라고 명령, 프레임을 그리고 프레임에 포함된 컨포넌트에 다시 그리라고 명령
public class GraphicsPractice extends JFrame {
	GraphicsPractice() {
		setTitle("Graphics Practice");
		setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		GraphicsPanel p = new GraphicsPanel();
		add(p);

		setVisible(true);
	}

	public static void main(String[] args) {
		new GraphicsPractice();
	}

}
