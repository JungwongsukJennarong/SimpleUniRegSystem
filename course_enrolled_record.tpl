<title>Enrollment Record</title>
<h1>Student Course Enrollment Record</h1>
<table>
<tr><th>Student ID</th><th>Course Code</th><th>Course Title</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>