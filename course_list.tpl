<title>Course List</title>
<h1>Course List</h1>
<table>
<tr><th>Course Code</th><th>Course Title</th><th>Credit</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>