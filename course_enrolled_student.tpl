<title>{{studentid_id}}</title>
<h1>Hello Student {{studentid_id}}! The Course You Have Enrolled</h1>
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