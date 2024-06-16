# desafioadl/services.py

from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    resultado = []
    for tarea in tareas:
        subtareas = tarea.subtareas.all()
        resultado.append({'tarea': tarea, 'subtareas': subtareas})
    return resultado

def crear_nueva_tarea(descripcion):
    nueva_tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(sub_tarea_id):
    SubTarea.objects.filter(id=sub_tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas_y_subtareas):
    for item in tareas_y_subtareas:
        tarea = item['tarea']
        subtareas = item['subtareas']
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")
