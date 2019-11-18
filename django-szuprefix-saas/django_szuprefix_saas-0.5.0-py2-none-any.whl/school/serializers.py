# -*- coding:utf-8 -*-
# author : 'denishuang'
from django_szuprefix.api.mixins import IDAndStrFieldSerializerMixin
from rest_framework.validators import UniqueTogetherValidator

from . import models, mixins, helper
from ..course.serializers import CourseNameSerializer
from rest_framework import serializers

import logging

log = logging.getLogger("django")


class SchoolSerializer(IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ('name', 'type', 'create_time')



class GradeSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Grade
        fields = ('name',)
        validators = [
            UniqueTogetherValidator(
                queryset=models.Grade.objects.all(),
                fields=['party', 'name'],
                message='相同记录已存在, 请不要重复创建.'
            )
        ]


class SessionSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = ('name',)
        validators = [
            UniqueTogetherValidator(
                queryset=models.Session.objects.all(),
                fields=['party', 'name'],
                message='相同记录已存在, 请不要重复创建.'
            )
        ]


class MajorSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    college_name = serializers.CharField(source="college.name", read_only=True)

    class Meta:
        model = models.Major
        # exclude = ('party',)
        fields = ('name', 'code', 'college', 'college_name', 'create_time')


class CollegeSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = models.College
        fields = ('name', 'code', 'create_time')
        validators = [
            UniqueTogetherValidator(
                queryset=models.College.objects.all(),
                fields=['party', 'name'],
                message='相同记录已存在, 请不要重复创建.'
            )
        ]


class ClazzSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    grade_name = serializers.CharField(source="grade.name", read_only=True)
    entrance_session_name = serializers.CharField(source="entrance_session.name", label="入学年份", read_only=True)

    student_names = serializers.JSONField(label="学生名单", required=False, allow_null=True)
    teacher_names = serializers.JSONField(label="老师名单", required=False, allow_null=True)

    class Meta:
        model = models.Clazz
        fields = ('name', 'short_name', 'entrance_session', 'entrance_session_name', 'code',
                  'primary_teacher', 'grade', 'grade_name', 'teacher_names', 'students', 'student_names')
        validators = [
            UniqueTogetherValidator(
                queryset=models.Clazz.objects.all(),
                fields=['party', 'name'],
                message='相同记录已存在, 请不要重复创建.'
            )
        ]

class ClazzNameSerializer(serializers.ModelSerializer):
    class Meta(ClazzSerializer.Meta):
        fields = ('name', )

class ClazzSmallSerializer(ClazzSerializer):
    class Meta(ClazzSerializer.Meta):
        fields = ('id', 'name', 'student_count', 'grade', 'entrance_session', 'grade_name', 'entrance_session_name')


class TeacherSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    user_name = serializers.CharField(label='帐号', source="user.username", read_only=True)
    courses = CourseNameSerializer(label='课程', many=True, read_only=True, source='courses.distinct')
    classes = ClazzNameSerializer(label='班级', many=True, read_only=True, source='classes.distinct')

    class Meta:
        model = models.Teacher
        fields = ('name', 'courses', 'classes', 'user_name')


class TeacherListSerializer(TeacherSerializer):
    class Meta(TeacherSerializer.Meta):
        fields = ()


class StudentSerializer(IDAndStrFieldSerializerMixin, mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    grade_name = serializers.CharField(source="grade.name", read_only=True)
    # clazz_name = serializers.CharField(source="clazz.name", read_only=True)
    class_names = serializers.CharField(label='班级', read_only=True)

    class Meta:
        model = models.Student
        fields = (
            'id', 'name', 'number', 'class_names', 'classes', 'grade', 'grade_name', 'courses', 'is_active',
            'is_bind'
        )


class CurrentStudentSerializer(mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    school = serializers.StringRelatedField()
    clazz = serializers.StringRelatedField()
    grade = serializers.StringRelatedField()
    entrance_session = serializers.StringRelatedField()

    class Meta:
        model = models.Student
        fields = ('name', 'number', 'grade', 'entrance_session', 'clazz', 'classes', 'school')


class CurrentTeacherSerializer(mixins.SchoolSerializerMixin, serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = models.Teacher
        fields = ('name', 'school')


class StudentBindingSerializer(serializers.Serializer):
    mobile = serializers.CharField(label="手机号", required=True)
    number = serializers.CharField(label="学号", required=True)
    name = serializers.CharField(label="姓名", required=True)
    the_id = serializers.IntegerField(label="指定ID", required=False)

    def validate(self, data):
        assert 'request' in self.context, 'needs context[request]'
        self.request = self.context['request']
        self.cur_user = cur_user = self.request.user
        if hasattr(cur_user, 'as_school_student'):
            raise serializers.ValidationError("当前帐号已绑定过,不能重复绑定")
        mobile = data['mobile']
        number = data['number']
        name = data['name']
        the_id = data.get('the_id')
        qset = models.Student.objects.filter(number=number, name=name)
        ss = []
        for s in qset:
            user = s.user
            if hasattr(user, 'as_person') and getattr(user, 'as_person').mobile == mobile:
                if not the_id or s.id == the_id:
                    ss.append(s)
        if not ss:
            raise serializers.ValidationError("相关账号不存在, 可能查询信息不正确, 或者还未录入系统")
        elif len(ss) == 1:
            if ss[0].is_bind == True:
                raise serializers.ValidationError("该帐号已绑定过,不能重复绑定")
        data['students'] = ss
        return data

    def save(self):
        students = self.validated_data['students']
        if len(students) == 1:
            student = students[0]
            log.info("StudentBindingSerializer bind user %s to %s" % (self.cur_user, student))
            helper.bind(student, self.cur_user)
            from django.contrib.auth import login
            login(self.request, student.user, backend='binding')
        return [unicode(s.school) for s in students]


class ClazzCourseSerializer(mixins.PartySerializerMixin, IDAndStrFieldSerializerMixin, serializers.ModelSerializer):
    clazz_name = serializers.CharField(source="clazz.name", label="班名", read_only=True)
    course_name = serializers.CharField(source="course.name", label="课名", read_only=True)
    teacher_name = serializers.CharField(source="teacher.name", label="老师", read_only=True)

    class Meta:
        model = models.ClazzCourse
        fields = ('clazz', 'course', 'teacher', 'clazz_name', 'course_name', 'teacher_name')
        validators = [
            UniqueTogetherValidator(
                queryset=models.ClazzCourse.objects.all(),
                fields=['clazz', 'course'],
                message='相同记录已存在, 请不要重复创建.'
            )
        ]
