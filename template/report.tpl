%include header.tpl
%include menu.tpl
%if not List:
	<div align="center" class="textbox">
	<form method="POST" action="/report" id="report">
		<p class="text">Отчет по расходам воды квартиры № <input type="text" name="apartment" size="2" maxlength="6" value=""> в доме № <input type="text" name="home" size="2" maxlength="6" value=""> <input type="submit" value="Показать"></p>
	</form>
%end
%if List:
	%if not home:
		<div align="center" class="textbox">
			<form method="POST" action="/report" id="report">
		<p class="text">Отчет по расходам воды квартиры № <input type="text" name="apartment" size="2" maxlength="6" value="{{List[0][2]}}"> в доме № <input type="text" name="home" size="2" maxlength="6" value="{{List[0][1]}}"> <input type="submit" value="Показать"></p>
		</form>
		<table class="table1">
			<thead>
				<tr>
					<th>Дата</th>
					<th scope="col" abbr="Starter">Холодная вода</th>
					<th scope="col" abbr="Medium">Горячая вода</th>
					<th scope="col" abbr="Business">Канализация</th>
				</tr>
			</thead>
			<tbody>
			%for x in List:
				<tr>
					<td>{{x[5]}}</td>
					<td>{{x[3]}}</td>
					<td>{{x[4]}}</td>
					<td>{{x[3]+x[4]}}</td>
				</tr>
			%end

			</tbody>
		</table>
	%end
	%if home:
		<div align="center" class="textbox">
			<form method="POST" action="/report" id="report">
		<p class="text">Отчет по расходам воды квартиры № <input type="text" name="apartment" size="2" maxlength="6" value="все"> в доме № <input type="text" name="home" size="2" maxlength="6" value="{{List[0][1]}}"> <input type="submit" value="Показать"></p>
		</form>
		<table class="table1">
			<thead>
				<tr>
					<th>Квартира</th>
					<th scope="col" abbr="Starter">Холодная вода</th>
					<th scope="col" abbr="Medium">Горячая вода</th>
					<th scope="col" abbr="Business">Канализация</th>
				</tr>
			</thead>
			<tfoot>
				<tr>
						<tr>
							<td>Итого</td>
							<td>{{sumcold}}</td>
							<td>{{sumhot}}</td>
							<td>{{sumhot + sumcold}}</td>
						</tr>
				</tr>
			</tfoot>
			<tbody>
			%for x in List:
				<tr>
					<td>{{x[2]}}</td>
					<td>{{x[3]}}</td>
					<td>{{x[4]}}</td>
					<td>{{x[3]+x[4]}}</td>
				</tr>
			%end

			</tbody>
		</table>
	%end
%end

</div>
%include footer.tpl