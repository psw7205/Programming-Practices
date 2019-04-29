package homework4;

import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

// 결과를 표시할 패널입니다
class Hw4ResultPanel extends JPanel {
	String result; // 계산결과를 표시할 문자열입니다

	Hw4ResultPanel() {
		result = "0"; // 맨 처음 0으로 초기화합니다
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;

		int w = this.getWidth();
		int h = this.getHeight(); // 패널의 크기를 얻어왔습니다

		int tmpRatio = h / 10; // 화면의 크기가 변하면 폰트사이즈, 여백등이 같이 변해야하기에 비율을 설정했습니다
		int fontSize = tmpRatio * 6;
		g2.setFont(new Font("Arial", Font.PLAIN, fontSize)); // 적당한 크기의 폰트를 설정했습니다

		FontMetrics tmp = g2.getFontMetrics(); // 오른쪽 정렬을 위해 글꼴의 정보를 얻어옵니다

		int sx = w - tmpRatio; // 처음 시작위치를 오른쪽 끝에서 살짝 왼쪽으로
		int sy = h / 2 + tmp.getAscent() / 2; // 중간으로 설정합니다

		for (int i = 0; i < result.length(); i++)
			sx -= tmp.charWidth(result.charAt(i)); // 각 글자의 길이만큼 왼쪽으로 시작점을 이동시켜 항상 오른쪽 정렬이 되도록 했습니다

		GradientPaint grayToDarkGray = new GradientPaint(0, 0, Color.GRAY, 0, h, Color.DARK_GRAY);
		g2.setPaint(grayToDarkGray); // Graphcis2D클래스의 그라데이션 사용입니다
		g2.fillRect(0, 0, w, h); // 패널 전부를 채웁니다

		g2.setColor(Color.WHITE);
		g2.drawString(result, sx + 1, sy + 1); // 그림자입니다
		g2.setColor(Color.BLACK);
		g2.drawString(result, sx, sy); // 문자열을 출력합니다
	}
}

class Hw4Button extends JButton {
	Hw4Button() {
		this.setName("14"); // 최초 공백 버튼의 이름을 14로 초기화했습니다
		// "" 그냥 공백으로 설정해봤지만 밑에 Name을 int형으로 변환하는데 ""에서 오류가 생겨 14로 초기화하고
		// ActionListener에서 처리했습니다
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		String str = this.getName(); // 각 버튼의 이름을 가져왔습니다
		int w = this.getWidth();
		int h = this.getHeight(); // 버튼의 크기를 가져왔습니다
		int offset = h / 10; // 버튼의 여백부분을 버튼 높이의 1/10으로 설정했습니다

		int fontSize = offset * 7;
		g.setFont(new Font("Arial", Font.BOLD, fontSize)); // 버튼의폰트를 설정했습니다

		g.setColor(new Color(255, 200, 150));
		g.fillRoundRect(offset, offset, w - offset * 2, h - offset * 2, 10, 10); // 버튼 속 둥근모서리의 사각형을 설정합니다

		g.setColor(Color.BLACK);

		switch (Integer.parseInt(str)) { // 이름을 정수로 변환했을 때
		case 10: // 10이면 clear입니다
			str = "C";
			g.setColor(Color.WHITE);
			g.drawString(str, w / 2 - offset * 2, h * 3 / 4 + 1);
			g.setColor(new Color(200, 100, 100));
			g.drawString(str, w / 2 - offset * 2, h * 3 / 4); // 글자를 설정하고
			return; // 종료합니다
		case 11: // 나머지의 경우 그냥 +, -, = 로 str문자열을 바꾸고 switch문을 탈출합니다
			str = "+";
			break;
		case 12:
			str = "-";
			break;
		case 13:
			str = "=";
			break;
		case 14: // 빈버튼 2개의 경우입니다
			str = "";
			break;

		default:
			break;
		}

		g.setColor(Color.WHITE);
		g.drawString(str, w / 2 - offset * 2 + 2, h * 3 / 4 + 2);
		g.setColor(new Color(100, 100, 100));
		g.drawString(str, w / 2 - offset * 2, h * 3 / 4);
		// 숫자버튼은 처음부터 버튼이름이 숫자였고 나머지는 switch문에서 변환되었으므로 그대로 출력합니다

	}
}

class Hw4Panel extends JPanel implements ActionListener {

	Hw4Button button[] = new Hw4Button[16]; // 버튼 16개입니다
	Hw4ResultPanel resultPanel; // 결과를 출력할 패널입니다

	int preResult; // 직전계산결과
	int result; // 계산결과
	int flag; // 계산결과를 바꿀 플래그
	int operation; // 연산자 저장 1, -1
	static final double ratio = 0.75; // 비율 변수들입니다

	Hw4Panel() {
		this.setLayout(null); // 배치관리자를 제거합니다
		operation = 1;
		flag = 0;

		resultPanel = new Hw4ResultPanel();
		this.add(resultPanel); // 결과 패널을 추가합니다

		for (int i = 0; i < 16; i++) {
			button[i] = new Hw4Button();
			button[i].addActionListener(this);
			this.add(button[i]);
		} // 버튼 16개의 액션리스너를 등록하고 패널에 추가합니다

		button[3].setName("10"); // clear
		button[7].setName("11"); // +
		button[11].setName("12"); // -
		button[12].setName("0"); // 0
		button[15].setName("13"); // =

		for (int i = 0; i < 3; i++) {
			button[i].setName("" + (i + 7));
			button[i + 4].setName("" + (i + 4));
			button[i + 8].setName("" + (i + 1));
		} // 버튼의 이름들을 설정합니다

	}

	@Override
	public void actionPerformed(ActionEvent e) {

		Hw4Button btn = (Hw4Button) e.getSource(); // 지금 액션은 버튼밖에 없으므로 강제형변환 후 사용했습니다
		int tmp = Integer.parseInt(btn.getName()); // 버튼의 이름을 정수로 변환합니다

		if (tmp == 14)
			return; // 14의 경우 공백 버튼입니다 아무일 없이 종료합니다

		switch (tmp) {

		case 10: // clear 할 경우
			result = 0;
			preResult = 0;
			flag = 0;
			operation = 1;
			break; // 초기화 합니다

		case 11: // +
		case 12: // -
		case 13: // =
			preResult += result * operation; // 이전결과에 현재 결과를 더하고
			result = 0; // 현재 결과를 새로 표시하기위해 0으로 초기화합니다

			if (tmp == 11)
				operation = 1;
			if (tmp == 12) // -의 경우
				operation = -1; // operation을 -1로 설정해 위에서 더하기만 하더라도 뺄셈이 되도록 했습니다

			flag = 0; // 계산결과를 출력하기위해 0으로 변경합니다
			break;

		default:
			result = result * 10 + tmp; // 기존 값을 한자리 쉬프트하고 더합니다
			flag = 1; // 현재 계산 중인 결과를 출력하기위해 1로 변경합니다
			break;
		}

		if (flag == 0)
			resultPanel.result = String.valueOf(preResult); // 누적계산결과를 저장합니다
		else
			resultPanel.result = String.valueOf(result); // 현재 입력중인 결과를 저장합니다

		this.repaint();
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		Graphics2D g2 = (Graphics2D) g;

		Point topLeftPoint = new Point(); // 계산기의 좌상단 좌표
		Point centerPoint = new Point(); // 계산기의 중심좌표
		int w; // 화면의 가로길이
		int h; // 화면의 세로 길이
		int calcWidth; // 계산기의 가로길이
		int calcHeigh; // 계산기의 세로길이

		w = this.getWidth();
		h = this.getHeight();
		centerPoint.x = w / 2;
		centerPoint.y = h / 2; // 현재 패널의 크기와 중심값을 설정합니다

		if (w / ratio > h) { // 가로비율이 더 긴 경우
			calcHeigh = h;
			calcWidth = (int) (h * ratio);
		} else { // 세로가 더 긴경우를 나누어 어느때에도 계산기의 형태가 유지되게 설정했습니다
			calcWidth = w;
			calcHeigh = (int) (w / ratio);
		}

		topLeftPoint.x = centerPoint.x - calcWidth / 2;
		topLeftPoint.y = centerPoint.y - calcHeigh / 2; // 계산기의 좌상단을 설정합니다

		g2.setColor(Color.BLACK);
		g2.fillRect(0, 0, w, h); // 패널 전체 배경을 검정으로 칠합니다

		GradientPaint gradient = new GradientPaint(0, 0, new Color(40, 70, 70), 0, this.getHeight(),
				new Color(150, 150, 150));
		g2.setPaint(gradient);
		// Graphics2D의 그라데이션을 이용해
		g.fillRect(topLeftPoint.x, topLeftPoint.y, calcWidth, calcHeigh);
		// 계산 결과를 출력할 패널의 배경을 칠합니다

		int offset = calcHeigh / 50;
		resultPanel.setBounds(topLeftPoint.x + offset, topLeftPoint.y + offset, calcWidth - offset * 2,
				calcHeigh / 3 - offset * 2);
		// 결과 출력패널의 범위를 설정합니다
		resultPanel.repaint();

		int buttonStartX = topLeftPoint.x;
		int buttonStartY = topLeftPoint.y + calcHeigh / 3;
		int buttonWidth = calcWidth / 4;
		int buttonHeigh = calcHeigh * 2 / 3 / 4;
		// 버튼의 시작좌표, 크기를 설정합니다

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				button[i * 4 + j].setBounds(buttonStartX + j * (buttonWidth + 1), buttonStartY + i * (buttonHeigh + 1),
						buttonWidth, buttonHeigh);
				// 버튼의 범위들를 설정합니다
				button[i].repaint();
			}
		}

	}

}

public class Hw4 extends JFrame {

	Hw4() {
		this.setTitle("Hw4");
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.add(new Hw4Panel());
		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Hw4();
	}

}
