﻿%include header.tpl%include menu.tpl<div align="center" class="textbox"><p class="text">Введите текущие показания счетчика</p><form action="/edit" method="POST"> <table class="table1">	<thead>		<tr>			<th scope="col" abbr="Starter">Холодная вода</th>			<th scope="col" abbr="Medium">Горячая вода</th>		</tr>	</thead>	<tfoot>		<tr>			<td></td>			<td><input type="submit" value="Обновить"></td>		</tr>	</tfoot>	<tbody>		<tr>			<td><input type="text" name="cold"></td>			<td><input type="text" name="hot"></td>				</tr>	</tbody>	</table></form></div>%include footer.tpl