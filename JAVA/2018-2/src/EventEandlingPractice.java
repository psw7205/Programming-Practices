import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class MyLabel extends JLabel implements ActionListener {

	@Override
	public void actionPerformed(ActionEvent arg0) {
		// 이벤트가 발생하면 이 함수가 호출됨
		JButton b = (JButton) arg0.getSource();
		String str = b.getText();

		if (str.equals("button"))
			b.setText("Click");
		else
			b.setText("button");

		setText(" l2 : 안녕하세요");
	}
}

class MyAction implements ActionListener {
	JLabel l;
	JPanel p;

	@Override
	public void actionPerformed(ActionEvent arg0) {
		// 이벤트가 발생하면 이 함수가 호출됨
		JButton b = (JButton) arg0.getSource();
		String str = b.getText();

		if (str.equals("button"))
			b.setText("Click");
		else
			b.setText("button");

		l.setText("l : 안녕하세요");
		p.setBackground(java.awt.Color.YELLOW);

	}

}

class EventHandlingPanel extends JPanel implements ActionListener { // 프레임은 프레임일 뿐 실제 버튼은 패널에서 관리
	JButton b;
	JLabel l;
	JButton b2;

	EventHandlingPanel() {

		b = new JButton("button");
		add(b);

		b2 = new JButton("button2");
		add(b2);

		MyAction act = new MyAction();

		l = new JLabel("l : hello world");
		MyLabel l2 = new MyLabel();

		l2.setText(" l2 : hewllo world");

		act.l = l;
		act.p = this;
		// b.addActionListener(l2); // 이 버튼의 액션을 처리할 수 있는 리스너를 등록
		// b.addActionListener(act);

		JPanel p = this;
		// 어차피 이 액션리스너는 이 클래스에서만 사용하니 그냥 anonymous class로 사용
		b.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				String str = b.getText();

				if (str.equals("button"))
					b.setText("Click");
				else
					b.setText("button");

				l.setText("anonymous class사용");
				l2.setText("~~~");

				p.setBackground(Color.GRAY);

			}

		});

		b2.addActionListener(this);
		b2.addMouseListener(new MouseListener() {

			@Override
			public void mouseClicked(MouseEvent arg0) {

			}

			@Override
			public void mouseEntered(MouseEvent arg0) {
				b2.setBackground(Color.RED);
			}

			@Override
			public void mouseExited(MouseEvent arg0) {
				b2.setBackground(Color.WHITE);
			}

			@Override
			public void mousePressed(MouseEvent arg0) {

			}

			@Override
			public void mouseReleased(MouseEvent arg0) {

			}

		});

		l2.addMouseListener(new MouseListener() {

			@Override
			public void mouseClicked(MouseEvent arg0) {
				l2.setText("마우스클릭으로 텍스트 변경");
			}

			@Override
			public void mouseEntered(MouseEvent arg0) {

			}

			@Override
			public void mouseExited(MouseEvent arg0) {

			}

			@Override
			public void mousePressed(MouseEvent arg0) {

			}

			@Override
			public void mouseReleased(MouseEvent arg0) {

			}

		});

		add(l);
		add(l2);

	}

	@Override
	public void actionPerformed(ActionEvent arg0) {

		// 이 경우 버튼을 구분 하기 위해선 함수 속에서 따로 조건문이 필요함
		if (arg0.getSource() == b) {
			String str = b.getText();

			if (str.equals("button"))
				b.setText("Click");
			else
				b.setText("button");

			l.setText("panel에 인터페이스를 추가해 구현");

			setBackground(java.awt.Color.PINK);
		}

		if (arg0.getSource() == b2) {
			String str = b.getText();

			if (str.equals("button"))
				b.setText("Click");
			else
				b.setText("button");

			l.setText("panel에 인터페이스를 추가해 구현");

			setBackground(Color.PINK);
		}

	}

}

public class EventEandlingPractice extends JFrame {

	EventEandlingPractice() {
		// 기본 셋팅 : 타이틀, 사이즈, x 버튼 누를 시 종료, 화면 출력
		this.setTitle("Event Handling Practice");
		this.setSize(400, 300);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		EventHandlingPanel p = new EventHandlingPanel();

		add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {

		new EventEandlingPractice();
	}

}
